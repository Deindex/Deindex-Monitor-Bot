import requests
from bs4 import BeautifulSoup


def check_noindex(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    meta = soup.find("meta", attrs={"name": "robots"})

    if not meta:
        return False

    return "noindex" in meta.get("content", "").lower()
