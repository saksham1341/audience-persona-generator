import streamlit as st

def github_link(repo_url: str):
    st.markdown(
        f"""
        <div style="text-align: left;">
            <a href="{repo_url}" target="_blank" style="text-decoration: none;">
                <img src="https://img.shields.io/badge/GitHub-Repository-red?logo=github"
                     alt="GitHub Repository"/>
            </a>
        </div>
        """,
        unsafe_allow_html=True,
    )
