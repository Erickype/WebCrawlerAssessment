from filters import count_words, filter_more_than_five, filter_five_or_less
from models import HackerNewsEntry

def test_count_words():
    assert count_words("This is - a self-explained example") == 5
    assert count_words("Hello, world!") == 2


def test_filter_more_than_five():
    entries = [
        HackerNewsEntry(1, "Short title", 10, 2),
        HackerNewsEntry(2, "This title has more than five words", 50, 15),
        HackerNewsEntry(3, "More comments has more than five words", 50, 30),
    ]
    filtered = filter_more_than_five(entries)
    assert len(filtered) == 2
    assert filtered[0].title.startswith("More comments")


def test_filter_five_or_less():
    entries = [
        HackerNewsEntry(1, "Short title", 10, 2),
        HackerNewsEntry(2, "Another one", 30, 0),
        HackerNewsEntry(3, "This title has more than five words", 50, 15),
    ]
    filtered = filter_five_or_less(entries)
    assert len(filtered) == 2
    assert filtered[0].title.startswith("Another one")
