from filters import count_words, filter_more_than_five, filter_five_or_less
from models import HackerNewsEntry

def test_count_words():
    assert count_words("This is - a self-explained example") == 5
    assert count_words("Hello, world!") == 2
