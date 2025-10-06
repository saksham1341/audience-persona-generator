"""
Landing page.
"""

import streamlit as st

st.title("AI Audience Persona Generator")
st.subheader("Stop Guessing. Know Your Audience Instantly.")
st.text("Tired of lengthy research and generic customer profiles? Describe your product and target demographic, and our AI will generate a detailed, data-driven marketing persona in seconds. Get a complete picture of your customer—from their goals and frustrations to their background story—so you can build better products and launch campaigns that actually convert.")
if st.button(
    label="Go to Persona Generator",
    key="go-to-persona-generator",
):
    st.switch_page("pages/generator.py")
