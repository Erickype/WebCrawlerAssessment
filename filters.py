import re
from crawler import fetch_entries
from models import HackerNewsEntry

def count_words(title: str) -> int:
    #Count words ignoring symbols
    words = re.sub(r"[^A-Za-z0-9\s]", "", title)
    return len(words.split())

if __name__ == '__main__':
    entries = fetch_entries()