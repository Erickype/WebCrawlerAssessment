import bs4
import requests
from bs4 import BeautifulSoup

from models import HackerNewsEntry

def fetch_entries(limit: int = 30)-> list[HackerNewsEntry]:
    url = "https://news.ycombinator.com/"
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select(".athing")[:limit]

    hacker_new_entries = []
    for row in rows:
        rank_text = row.select_one(".rank")
        title_text = row.select_one(".titleline a")

        rank = int(rank_text.text.strip("."))
        title = title_text.text

        #Extract from subtext
        subtext = row.find_next_sibling("tr").select_one(".subtext")

        points = (
            int(subtext.select_one(".score").text.split(" ")[0])
            if subtext.select_one(".score")
            else -1
        )
        number_comments_link: bs4.Tag = subtext.find_all("a")[-1]
        number_comments = (
            int(number_comments_link.text.split()[0])
            if "comment" in number_comments_link.text
            else -1
        )

        hacker_news_entry = HackerNewsEntry(rank, title, points, number_comments)
        hacker_new_entries.append(hacker_news_entry)

    return hacker_new_entries

if __name__ == "__main__":
    entries = fetch_entries()

    for entry in entries:
        print(entry)