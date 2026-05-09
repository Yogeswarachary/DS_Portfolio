# pages/resume.py

import streamlit as st
from pathlib import Path
from config import SITE, EXPERIENCE, EDUCATION, CERTIFICATIONS, SUMMARY
from utils import section_header, card

ROOT_DIR = Path(__file__).resolve().parent.parent


def show():
    section_header("Resume")

    # Download button
    resume_path = ROOT_DIR / SITE["resume_file"]
    if resume_path.exists():
        st.download_button(
            "📄 Download Full Resume (PDF)",
            data=resume_path.read_bytes(),
            file_name="Yogeswarachary_Resume.pdf",
            mime="application/pdf",
        )

    st.markdown(SUMMARY, unsafe_allow_html=True)
    st.markdown("---")

    # Experience
    section_header("Experience")
    for exp in EXPERIENCE:
        bullets_html = "".join(f"<li>{b}</li>" for b in exp["bullets"])
        card(
            f"""
            <h4>{exp['role']}</h4>
            <p><strong>{exp['company']}</strong> · {exp['location']} · {exp['duration']}</p>
            <ul>{bullets_html}</ul>
            """
        )
        st.write("")

    st.markdown("---")

    # Education
    section_header("Education")
    for edu in EDUCATION:
        card(
            f"""
            <h4>{edu['degree']}</h4>
            <p><strong>{edu['institution']}</strong> · {edu['duration']}</p>
            """
        )
        st.write("")

    st.markdown("---")

    # Certifications
    section_header("Certifications")
    cols = st.columns(3)
    for i, cert in enumerate(CERTIFICATIONS):
        with cols[i % 3]:
            card(f"<h5>{cert['name']}</h5><p>{cert['issuer']}</p>")
            st.write("")