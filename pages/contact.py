# pages/contact.py

import streamlit as st
from config import SITE
from utils import section_header, card


def show():
    section_header(
        "Contact",
        "Actively seeking Entry-Level or Junior Data Science · ML Engineering · Analytics roles",
    )

    col1, col2 = st.columns([1, 1])

    with col1:
        card(
            f"""
            <h4>Get in touch</h4>
            <p>📧 <a href="mailto:{SITE['email']}">{SITE['email']}</a></p>
            <p>📱 {SITE['phone']}</p>
            <p>📍 {SITE['location']}</p>
            <hr>
            <p>
                <a href="{SITE['github']}" target="_blank">🐙 GitHub</a> &nbsp;|&nbsp;
                <a href="{SITE['linkedin']}" target="_blank">🔗 LinkedIn</a> &nbsp;|&nbsp;
                <a href="{SITE['research_paper']}" target="_blank">📄 Research Paper</a>
            </p>
            """
        )

    with col2:
        card(
            """
            <h4>Response Times</h4>
            <p>📧 Email — within 12 hours</p>
            <p>💬 LinkedIn — within 2–6 hours</p>
            <p>📱 WhatsApp — within 2–6 hours</p>
            <hr>
            <p>👔 Available for interviews weekdays & weekends</p>
            """
        )

    st.markdown(
        f"""<div style="text-align:center; margin-top:1.5rem;">
            <a class="link-btn accent" href="mailto:{SITE['email']}">📧 Email Me Directly</a>
        </div>""",
        unsafe_allow_html=True,
    )