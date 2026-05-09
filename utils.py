import streamlit as st
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent


def load_css():
    """Inject style.css into the Streamlit app."""
    css_path = ROOT_DIR / "assets" / "style.css"
    if css_path.exists():
        st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)


def card(html: str):
    """Wrap any HTML content in a glass card."""
    st.markdown(f'<div class="glass-card">{html}</div>', unsafe_allow_html=True)


def section_header(title: str, subtitle: str = ""):
    """Render a consistent section heading with optional subtitle."""
    sub = f'<p class="section-sub">{subtitle}</p>' if subtitle else ""
    st.markdown(
        f'<div class="section-header"><h2>{title}</h2>{sub}</div>',
        unsafe_allow_html=True,
    )


def skill_badges(labels: list):
    """Render a row of pill-shaped skill badges."""
    badges = " ".join(f'<span class="skill-badge">{s}</span>' for s in labels)
    st.markdown(badges, unsafe_allow_html=True)


def link_buttons(github: str = "", app: str = "", paper: str = ""):
    """Render a row of GitHub / Live App / Paper link buttons."""
    btns = []
    if github:
        btns.append(f'<a class="link-btn" href="{github}" target="_blank">GitHub</a>')
    if app:
        btns.append(f'<a class="link-btn accent" href="{app}" target="_blank">Live App ↗</a>')
    if paper:
        btns.append(f'<a class="link-btn" href="{paper}" target="_blank">Paper ↗</a>')
    st.markdown('<div class="btn-row">' + " ".join(btns) + "</div>", unsafe_allow_html=True)