


    
  
"""Display index.html as a full-viewport, borderless Streamlit page.

Place index.html next to this app.py in your GitHub repository.
"""

from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="CIFAL AI Capacity Map",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_file = Path(__file__).resolve().parent / "index.html"

if html_file.is_file():
    # Remove Streamlit's header, margins, padding, and background.
    # Fix the iframe directly to the viewport so it truly fills the screen.
    st.markdown(
        """
        <style>
        html, body, .stApp,
        [data-testid="stAppViewContainer"],
        [data-testid="stMain"] {
            margin: 0 !important;
            padding: 0 !important;
            overflow: hidden !important;
        }

        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stSidebar"],
        [data-testid="stBottom"],
        footer, #MainMenu {
            display: none !important;
        }

        .block-container,
        [data-testid="stMainBlockContainer"] {
            max-width: none !important;
            width: 100% !important;
            padding: 0 !important;
            margin: 0 !important;
        }

        iframe {
            position: fixed !important;
            inset: 0 !important;
            width: 100vw !important;
            height: 100vh !important;
            height: 100dvh !important;
            display: block !important;
            border: 0 !important;
            border-radius: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            z-index: 9999 !important;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.iframe(html_file, width="stretch", height=900)
else:
    st.error(
        "Could not find index.html. Upload it to the same folder "
        "as app.py in your GitHub repository."
    )
