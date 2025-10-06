# AI Powered Audience Persona Generator

Stop guessing. Know your audience instantly. This project is a web application built with **Streamlit** and **LangChain** that generates detailed, realistic marketing personas from a simple product description and target audience.

It helps marketers, founders, and creators build better products and launch smarter campaigns by truly understanding who they're selling to.

## Live

Hosted on render [here](https://audience-persona-generator.onrender.com/)!

![Sample](sample.gif)

## How It Works

The generator uses a sophisticated two-step AI process to create nuanced and detailed personas:

1.  **Demographic Parsing:** The app first takes the unstructured `target demographic` text and uses an LLM to extract and infer structured data. It intelligently identifies attributes like age range, gender, occupations, and lifestyle, even if they aren't explicitly stated.

2.  **Persona Generation:** It then combines this structured demographic data with the `product description` and feeds it into a second, more creative LLM prompt. This prompt generates a complete, narrative-driven persona with a name, background story, personality traits, goals, and frustrations.

## Key Features

- **Intuitive UI:** A clean and simple interface built with Streamlit for ease of use.
- **Intelligent Data Extraction:** Automatically parses and structures demographic information.
- **Rich Persona Narratives:** Generates personas with detailed backstories, goals, and pain points.
- **JSON-Powered:** Uses Pydantic for robust, structured LLM outputs, ensuring reliability.

## Tech Stack

- **Backend:** Python
- **Web Framework:** Streamlit
- **LLM Orchestration:** LangChain
- **Data Validation:** Pydantic
- **LLM Provider:** Google Gemini

## Run the project

```sh
# Activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Rename .env.example to .env and fill it (basically, set the environment variables any way you prefer)
mv .env.example .env

# Run the streamlit app (using dotenv here, depends on the way you want to load environment variables)
dotenv run -- streamlit run app.py
```

## Project Structure

```txt
|___ src/                # Core logic for the application
|   |___ generator.py    # Persona generation and demographic parsing
|   |___ models.py       # LLM model definitions and configurations
|___ pages/              # Streamlit pages for the multi-page app
|   |___ generator.py    # The main persona generator page UI
|   |___ index.py        # The application's home/landing page
|___ app.py              # Main Streamlit application entry point
|___ config.py           # Project-wide configurations
|___ requirements.txt    # Python package dependencies
|___ README.md           # You are here!
```
