# pages/projects.py

import streamlit as st
from config import PROJECTS
from utils import section_header, card, link_buttons, skill_badges


def show():
    section_header(
        "Projects",
        f"{len(PROJECTS)} total projects across fraud detection, analytics, GenAI, SQL, and ML",
    )

    all_categories = sorted({p["category"] for p in PROJECTS})
    all_tech = sorted({t for p in PROJECTS for t in p["tech"]})

    col1, col2 = st.columns(2)
    with col1:
        selected_category = st.selectbox("Filter by category", ["All"] + all_categories)
    with col2:
        selected_tech = st.multiselect("Filter by technology", all_tech, placeholder="All technologies")

    filtered = PROJECTS

    if selected_category != "All":
        filtered = [p for p in filtered if p["category"] == selected_category]

    if selected_tech:
        filtered = [p for p in filtered if any(t in selected_tech for t in p["tech"])]

    st.markdown(f"**Showing {len(filtered)} project(s)**")

    cols = st.columns(2)
    for i, proj in enumerate(filtered):
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