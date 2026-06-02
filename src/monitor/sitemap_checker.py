import requests


def check_sitemap(domain):

    sitemap_url = f"{domain}/sitemap.xml"

    try:

        response = requests.get(sitemap_url)

        return response.status_code == 200

    except Exception:

        return False
