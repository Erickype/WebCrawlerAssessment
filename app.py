import streamlit as st

st.set_page_config(page_title="WebCrawler", layout="wide")
st.title("Web Crawler Assessment")

entries = {}
st.success(f"Fetched {len(entries)} entries from Hacker News!")

option = st.radio(
    "Choose a filter:",
    [
        "More than five words (sorted by comments)",
        "Five or fewer words (sorted by points)",
    ],
)
