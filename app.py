import streamlit as st
from streamlit_option_menu import option_menu
from config import SITE
from utils import load_css

import pages.home     as home_page
import pages.projects as projects_page
import pages.about    as about_page
import pages.resume   as resume_page
import pages.contact  as contact_page

st.set_page_config(
    page_title=SITE["title"],
    page_icon=SITE["icon"],
    layout="wide",
    initial_sidebar_state="expanded",
)

load_css()

with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; padding: 0.2rem 0 0.8rem;">
            <h2 style="margin:0; font-size:1.35rem;">{SITE['name']}</h2>
            <p style="margin:0.35rem 0 0; font-size:0.95rem; color:#94a3b8;">{SITE['tagline']}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    selected = option_menu(
        menu_title=None,
        options=["Home", "Projects", "About", "Resume", "Contact"],
        icons=["house", "code-slash", "person", "file-earmark-text", "envelope"],
        default_index=0,
        styles={
            "container": {
                "background-color": "#020617",
                "padding": "0!important",
                "margin-top": "0.2rem",
            },
            "icon": {"color": "#e2e8f0", "font-size": "18px"},
            "nav-link": {
                "font-size": "18px",
                "text-align": "left",
                "margin": "4px 0",
                "padding": "12px 14px",
                "--hover-color": "rgba(0,210,255,0.12)",
                "border-radius": "10px",
            },
            "nav-link-selected": {
                "background-color": "#00d2ff",
                "color": "#0f172a",
                "font-weight": "700",
                "border-radius": "10px",
            },
        },
    )

# Page routing
pages = {
    "Home":     home_page,
    "Projects": projects_page,
    "About":    about_page,
    "Resume":   resume_page,
    "Contact":  contact_page,
}

pages[selected].show()