import requests


def check_robots(domain):

    robots_url = f"{domain}/robots.txt"

    try:

        response = requests.get(robots_url, timeout=10)

        return response.status_code == 200

    except Exception:

        return False
