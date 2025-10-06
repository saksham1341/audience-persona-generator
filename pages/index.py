"""
Landing page.
"""

import streamlit as st

st.title("AI Audience Persona Generator")
st.subheader("Stop Guessing. Know Your Audience Instantly.")

st.markdown("""
This project is a web application built with **Streamlit** and **LangChain** that generates detailed, realistic marketing personas from a simple product description and target audience.

It helps marketers, founders, and creators build better products and launch smarter campaigns by truly understanding who they're selling to.

## How It Works

The generator uses a sophisticated two-step AI process to create nuanced and detailed personas:

1.  **Demographic Parsing:** The app first takes the unstructured `target demographic` text and uses an LLM to extract and infer structured data. It intelligently identifies attributes like age range, gender, occupations, and lifestyle, even if they aren't explicitly stated.

2.  **Persona Generation:** It then combines this structured demographic data with the `product description` and feeds it into a second, more creative LLM prompt. This prompt generates a complete, narrative-driven persona with a name, background story, personality traits, goals, and frustrations.

## Key Features

- **Intuitive UI:** A clean and simple interface built with Streamlit for ease of use.
- **Intelligent Data Extraction:** Automatically parses and structures demographic information.
- **Rich Persona Narratives:** Generates personas with detailed backstories, goals, and pain points.
- **JSON-Powered:** Uses Pydantic for robust, structured LLM outputs, ensuring reliability.
""")

if st.button(
    label="Go to Persona Generator",
    key="go-to-persona-generator",
):
    st.switch_page("pages/generator.py")
