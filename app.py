from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="CGN 2026 Mapping",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_file = Path(__file__).resolve().parent / "index.html"

if html_file.is_file():
    st.iframe(html_file, width="stretch", height=900)
else:
    st.error(
        "HTML file not found. Add 'index.html' to the same folder as 'app.py' "
        "in your GitHub repository."
    )
