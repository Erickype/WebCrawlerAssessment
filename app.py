import streamlit as st
import pandas as pd

from crawler import fetch_entries

@st.cache_data(ttl=600)
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

#Data table
df = pd.DataFrame(entries)

st.data_editor(
    df,
    column_config={
        "rank": st.column_config.NumberColumn(
            "N°",
            help="Hacker News Number ",
        ),
        "title": st.column_config.TextColumn(
            "Title",
            help="Title of the article",
        ),
        "points": st.column_config.NumberColumn(
            "Points",
            help="Points given to the article ",
        ),
        "comments": st.column_config.NumberColumn(
            "N° comments",
            help="Number of comments for the article",
        ),
    },
    hide_index=True
)