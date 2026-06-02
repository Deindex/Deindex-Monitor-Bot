import requests


def check_url(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            return True

        return False

    except Exception:
        return False
