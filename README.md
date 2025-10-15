# Web Crawler Assessment

This is an assessment project containing a basic web crawler
with web scrapping techniques.

It tests the URL **https://news.ycombinator.com/** extracting the
first 30 entries. Considering just **the number, the title, 
the points, and the number of comments** for each entry

## Features
- Scrapes the first 30 Hacker News posts
- Displays data (rank, title, points, comments)
- Two filtering modes:
  1. Titles with more than five words → ordered by comments
  2. Titles with five or fewer words → ordered by points
- Fully interactive web UI
- Automated tests with Pytest

## Tech Stack

- Python 3.13
- Streamlit
- BeautifulSoup
- Pytest
- GitFlow branching model

## Environment Requisites

- Git latest version
- Python version 3.13

## Execution instructions

Clone the repository
```
git clone https://github.com/Erickype/WebCrawlerAssessment
```
```
cd WebCrawlerAssessment
```

It is recommended to use an environment **.venv**, see more here:
https://docs.python.org/3/library/venv.html. After creating the environment or not:
```
pip install -r requirements.txt
```

### Run Tests

```
python -m pytest -v
```

### Execute in localhost

```
streamlit run ./app.py
```