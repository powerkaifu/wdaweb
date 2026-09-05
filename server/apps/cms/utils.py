import io
import os
import logging
from PIL import Image
from django.core.files.base import ContentFile

logger = logging.getLogger(__name__)

def optimize_image(image_field, max_width=1920, quality=80):
    """
    自動化圖片處理管道：
    1. 若未上傳圖片則直接返回。
    2. 若當前使用的是 Cloudinary 雲端圖床儲存，直接返回交由 Cloudinary CDN 處理，
       避免二次上傳衝突與 Render 512MB 記憶體溢出。
    3. 本地儲存時，自動將圖片等比縮放至最大寬度 max_width，並轉換為 WebP 格式。
    4. 支援透明度 (RGBA / LA / P 模式)，並具備指標歸零防禦。
    """
    if not image_field or not bool(image_field):
        return

    # 若使用 Cloudinary 雲端圖床儲存，圖片處理與 WebP 轉換一律交由 Cloudinary CDN 雲端管線，本地不進行重複壓縮與提早上傳
    storage = getattr(image_field, 'storage', None)
    if storage:
        storage_cls_name = storage.__class__.__name__
        if 'Cloudinary' in storage_cls_name:
            logger.info(f"[Image Optimizer] 偵測到 Cloudinary 雲端圖床儲存，略過本地 PIL 壓縮，交由 CDN 雲端管線處理: {image_field.name}")
            return

    try:
        if not hasattr(image_field, 'file') or not image_field.file:
            return
    except Exception:
        # 當底層 storage 不支援 open 時直接略過
        return

    try:
        # 重設檔案指針至開頭
        if hasattr(image_field, 'seek'):
            try:
                image_field.seek(0)
            except Exception:
                pass

        # 開啟圖片
        img = Image.open(image_field)
        
        # 若已經是 WebP 且尺寸符合限制，直接返回避免重複存檔與產生隨機後綴
        if image_field.name.lower().endswith('.webp') and img.width <= max_width and getattr(img, 'format', None) == 'WEBP':
            return

        # 取得純檔名 (不含副檔名)
        name, _ = os.path.splitext(os.path.basename(image_field.name))

        # 1. 智慧等比縮小
        if img.width > max_width:
            ratio = max_width / float(img.width)
            new_height = int(float(img.height) * float(ratio))
            img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)

        # 2. 轉換為 WebP (處理 RGBA 透明度)
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            format_type = 'WEBP'
        else:
            img = img.convert('RGB')
            format_type = 'WEBP'

        # 輸出成 WebP byte stream
        output = io.BytesIO()
        img.save(output, format=format_type, quality=quality, method=6)
        output.seek(0)

        # 替換副檔名為 .webp
        new_name = f"{name}.webp"
        image_field.save(new_name, ContentFile(output.read()), save=False)
    except Exception as e:
        # 若圖片解析失敗則保留原圖，不阻擋儲存流程
        logger.warning(f"[Image Optimizer Warning] 無法壓縮圖片 {image_field.name}: {e}")
    finally:
        # 關鍵防禦：保證檔案指標重設回開頭，避免後續 Django save 流程讀取到空檔案
        if hasattr(image_field, 'seek'):
            try:
                image_field.seek(0)
            except Exception:
                pass
