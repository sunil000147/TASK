import streamlit as st
import pandas as pd
from src.research_agent import research_industry
from src.use_case_agent import generate_use_case_and_description

st.title("Multi-Agent Workflow: Industry Research & Use Cases")

company_name = st.text_input("Enter Company Name")
industry_name = st.text_input("Enter Industry Name")

if st.button("Generate"):
    st.write("Researching...")
    industry_info = research_industry(company_name, industry_name)

    if isinstance(industry_info, dict) and "error" in industry_info:
        st.error(industry_info["error"])
    else:
        for item in industry_info:
            use_case, description = generate_use_case_and_description(company_name, item["snippet"])
            st.write(f"**Use Case:** {use_case}")
            st.write(f"**Description:** {description}")
