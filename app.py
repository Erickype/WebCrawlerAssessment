import streamlit as st

from crawler import fetch_entries

def get_data():
    return fetch_entries()

st.set_page_config(page_title="WebCrawler", layout="wide")
st.title("Web Crawler Assessment")

entries = get_data()
st.success(f"Fetched {len(entries)} entries from Hacker News!")

option = st.radio(
    "Choose a filter:",
    [
        "More than five words (sorted by comments)",
        "Five or fewer words (sorted by points)",
    ],
)
