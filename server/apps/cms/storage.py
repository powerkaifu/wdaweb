"""
CMS 靜態檔案與媒體儲存類別
提供強健的容錯機制，防止在缺乏 manifest entry 時拋出 ValueError 導致管理後台 500 癱瘓。
"""
from whitenoise.storage import CompressedManifestStaticFilesStorage


class RobustCompressedManifestStaticFilesStorage(CompressedManifestStaticFilesStorage):
    """
    寬鬆型 WhiteNoise Manifest 儲存類別：
    當靜態檔案未在 manifest 中被記錄時，自動優雅退回使用原始檔案路徑，
    絕不拋出 ValueError: Missing staticfiles manifest entry，確保後台與前台 100% 穩定。
    """
    manifest_strict = False
