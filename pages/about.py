# pages/about.py

import streamlit as st
from utils import section_header, card


def show():
    section_header("About Me")

    st.markdown(
        """
My path to Data Science isn't traditional — and that's my strength.
With almost **3 years as a Visa Consultant & Process Analyst**, I developed obsessive
attention to detail, regulatory rigor, and the ability to identify anomalies under pressure.
I processed **100+ visa applications with zero compliance errors** and optimized workflows
that improved turnaround time by **50%**.

I realized my passion wasn't in regulatory documents — it was in **solving problems with data**.
Today I build models that don't just predict — they **add measurable business value**.
        """
    )

    st.markdown("---")
    section_header("My Working Principles")

    principles = [
        ("🏗️ Production-grade", "Every model is documented, tested, and deployable. No shortcuts."),
        ("📐 Evidence-driven", "Statistical rigor validates assumptions before implementation."),
        ("🗣️ Communication", "I bridge the gap between data insights and business impact."),
        ("🔧 Value-focused", "If it doesn't add value, it doesn't get shipped."),
    ]

    cols = st.columns(2)
    for i, (title, text) in enumerate(principles):
        with cols[i % 2]:
            card(f"<h4>{title}</h4><p>{text}</p>")
            st.write("")