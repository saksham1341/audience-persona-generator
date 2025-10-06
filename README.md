# AI Powered Audience Persona Generator

**WIP**

## Run the project

```sh
# Activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
python -m pip install -r requirements.txt

# Run the streamlit app
dotenv run -- streamlit run app.py
```

## Project Structure

```txt
|___ src/
    |___ generator.py  # Persona generator module
    |___ models.py  # LLM models defined here
|___ app.py  # Main app module
|___ config.py  # Project Configurations
|___ README.md  # Project Description
```
