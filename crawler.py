import bs4
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

        #Extract from subtext
        subtext = row.find_next_sibling("tr").select_one(".subtext")

        points = int(subtext.select_one(".score").text.split(" ")[0])
        number_comments_link: bs4.Tag = subtext.findAll("a")[-1]
        number_comments = int(number_comments_link.text.split()[0])

if __name__ == "__main__":
    fetch_entries()