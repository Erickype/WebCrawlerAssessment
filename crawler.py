import requests
from bs4 import BeautifulSoup

def fetch_entries(limit: int = 30):
    url = "https://news.ycombinator.com/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select(".athing")[:limit]

    for row in rows:
        rank_text = row.select_one(".rank")
        title_text = row.select_one(".titleline a")

        rank = int(rank_text.text.strip("."))
        title = title_text.text

if __name__ == "__main__":
    fetch_entries()