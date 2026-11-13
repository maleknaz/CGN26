"""Full-screen CIFAL dashboards with two tabs.

Place this file alongside:
  - index.html  (CIFAL Centers, the default tab)
  - hosts.html  (CIFAL Hosts)
"""

from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent
CENTERS_HTML = ROOT / "index.html"
HOSTS_HTML = ROOT / "hosts.html"
TAB_HEIGHT = 56  # Also used in the CSS below.

st.set_page_config(
    page_title="CIFAL AI Capacity Map",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Keep Streamlit chrome hidden, retain a small tab bar, and let the active
# HTML dashboard occupy all remaining browser space.
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

      /* The only visible Streamlit UI is this tab navigation. */
      .stTabs [data-baseweb="tab-list"] {
          position: fixed !important;
          top: 0 !important;
          left: 0 !important;
          right: 0 !important;
          height: 56px !important;
          z-index: 10000 !important;
          background: #102b40 !important;
          border-bottom: 1px solid #2e5062 !important;
          padding: 0 18px !important;
          gap: 4px !important;
          box-sizing: border-box !important;
      }

      .stTabs [data-baseweb="tab"] {
          height: 56px !important;
          padding: 0 22px !important;
          color: #c5d6de !important;
          font-size: 15px !important;
          font-weight: 600 !important;
          background: transparent !important;
      }
      .stTabs [data-baseweb="tab"][aria-selected="true"] {
          color: #ffffff !important;
          background: #1c4659 !important;
      }
      .stTabs [data-baseweb="tab-highlight"] {
          background: #49c7bc !important;
      }
      .stTabs [data-baseweb="tab-border"] {
          display: none !important;
      }

      /* Each dashboard fills the viewport beneath the tab strip. */
      .stTabs iframe {
          position: fixed !important;
          top: 56px !important;
          left: 0 !important;
          width: 100vw !important;
          height: calc(100vh - 56px) !important;
          height: calc(100dvh - 56px) !important;
          display: block !important;
          border: 0 !important;
          border-radius: 0 !important;
          margin: 0 !important;
          padding: 0 !important;
          z-index: 1 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

centers_tab, hosts_tab = st.tabs(
    ["CIFAL Centers", "CIFAL Hosts"],
    default="CIFAL Centers",
    key="cifal_navigation",
    on_change="rerun",  # Only load the selected dashboard.
)


def show_dashboard(file_path: Path, label: str) -> None:
    if file_path.is_file():
        st.iframe(file_path, width="stretch", height=900)
    else:
        st.error(
            f"Cannot find '{file_path.name}'. Add it to the same "
            "GitHub folder as app.py, then redeploy."
        )


if centers_tab.open:
    with centers_tab:
        show_dashboard(CENTERS_HTML, "CIFAL Centers")

if hosts_tab.open:
    with hosts_tab:
        show_dashboard(HOSTS_HTML, "CIFAL Hosts")
