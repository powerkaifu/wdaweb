import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.utils import timezone
from apps.cms.models import SiteSetting

def favicon_view(request):
    """處理 /favicon.ico 請求，優先使用後台上傳的 Logo 或 Favicon"""
    try:
        setting = SiteSetting.objects.first()
        if setting and setting.favicon:
            return HttpResponseRedirect(setting.favicon.url)
        if setting and setting.site_logo:
            return HttpResponseRedirect(setting.site_logo.url)
    except Exception:
        pass

    fallback_path = settings.BASE_DIR / 'static' / 'images' / 'logo.png'
    if os.path.exists(fallback_path):
        return FileResponse(open(fallback_path, 'rb'), content_type='image/png')
    return HttpResponseRedirect('/static/images/logo.png')

def robots_txt_view(request):
    host = request.build_absolute_uri('/')[:-1]
    lines = [
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {host}/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")

def sitemap_xml_view(request):
    host = request.build_absolute_uri('/')[:-1]
    today = timezone.now().strftime('%Y-%m-%d')
    
    xml_entries = [
        f"""  <url>
    <loc>{host}/</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>""",
        f"""  <url>
    <loc>{host}/#batches</loc>
    <lastmod>{today}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>""",
        f"""  <url>
    <loc>{host}/#curriculum</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""",
        f"""  <url>
    <loc>{host}/#showcase</loc>
    <lastmod>{today}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>""",
        f"""  <url>
    <loc>{host}/#faq</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.7</priority>
  </url>""",
        f"""  <url>
    <loc>{host}/#contact</loc>
    <lastmod>{today}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
    ]

    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{chr(10).join(xml_entries)}
</urlset>"""

    return HttpResponse(sitemap_xml, content_type="application/xml; charset=utf-8")
