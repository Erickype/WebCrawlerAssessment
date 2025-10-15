import re
from crawler import fetch_entries
from models import HackerNewsEntry

def count_words(title: str) -> int:
    #Count words ignoring symbols
    words = re.sub(r"[^A-Za-z0-9\s]", "", title)
    return len(words.split())


def filter_more_than_five(hacker_news_entries: list[HackerNewsEntry]) -> list[HackerNewsEntry]:
    return sorted(
        [e for e in hacker_news_entries if count_words(e.title) > 5],
        key=lambda e: e.comments,
        reverse=True,
    )



if __name__ == '__main__':
    entries = fetch_entries()
    print(filter_more_than_five(entries))