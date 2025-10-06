"""
Main app.
"""

import streamlit as st

_ = st.navigation(
    pages=["pages/index.py", "pages/generator.py", ],
    position="hidden"
)
_.run()
