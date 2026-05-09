# pages/home.py

import streamlit as st
from pathlib import Path
from config import SITE, SUMMARY, SKILLS, PROJECTS
from utils import section_header, skill_badges, card, link_buttons

ROOT_DIR = Path(__file__).resolve().parent.parent


def show():
    featured_projects = [p for p in PROJECTS if p.get("featured", False)]

    st.markdown(
        f"""
        <div class="hero">
            <h1 class="gradient-text">{SITE['name']}</h1>
            <p class="hero-tagline">{SITE['tagline']}</p>
            <p class="hero-sub">Fraud Detection · Analytics · GenAI Apps</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col_left, col_right = st.columns([1.8, 1])
    with col_left:
        st.markdown(SUMMARY, unsafe_allow_html=True)
        st.markdown(
            f"""<div class="contact-row">
                <a href="mailto:{SITE['email']}">📧 {SITE['email']}</a>
                <a href="{SITE['github']}" target="_blank">🐙 GitHub</a>
                <a href="{SITE['linkedin']}" target="_blank">🔗 LinkedIn</a>
            </div>""",
            unsafe_allow_html=True,
        )
    with col_right:
        resume_path = ROOT_DIR / SITE["resume_file"]
        if resume_path.exists():
            st.download_button(
                "📄 Download Resume",
                data=resume_path.read_bytes(),
                file_name="Yogeswarachary_Resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )

    st.markdown("---")

    section_header("Technical Skills")
    cols = st.columns(len(SKILLS))
    for col, (cat, items) in zip(cols, SKILLS.items()):
        with col:
            st.markdown(f"**{cat}**")
            skill_badges(items)

    st.markdown("---")

    section_header(
        "Featured Projects",
    )

    cols = st.columns(2)
    for i, proj in enumerate(featured_projects):
        with cols[i % 2]:
            card(
                f"""
                <h3>{proj['icon']} {proj['title']}</h3>
                <p>{proj['desc']}</p>
                <p><strong>Category:</strong> {proj['category']}</p>
                <span class="highlight-badge">{proj['highlight']}</span>
                """
            )
            skill_badges(proj["tech"])
            link_buttons(
                github=proj.get("github", ""),
                app=proj.get("app", ""),
                paper=proj.get("paper", ""),
            )
            st.write("")