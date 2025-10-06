"""
Streamlit Persona Generator Page
"""

from src.generator import parse_demographic, generate_persona
import streamlit as st
from time import sleep

st.title("Generate an audience persona for your product")
st.divider()

def stream_into_empty_container(container, text, speed = 10):
    r = ""
    container.markdown(r)
    for x in text:
        r += x
        container.markdown(r)
        sleep(1 / (speed ** 2))

if "messages" not in st.session_state:
    st.session_state.messages = [{
        "type": "ai",
        "content": [
            "Hey there!",
            "To generate an audience persona, first give me your product details."
        ]
    }]
    st.session_state.progress = 0

for msg in st.session_state.messages[:-1]:
    with st.chat_message(msg["type"]):
        for txt in msg["content"]:
            st.markdown(txt)

last_message = st.session_state.messages[-1]
with st.chat_message(last_message["type"]):
    for txt in last_message["content"]:
        _ = st.empty()
        stream_into_empty_container(_, txt)

if len(st.session_state.messages) == 1:
    def _():
        st.session_state.messages.append({
            "type": "user",
            "content": [
                st.session_state.chat_input,
            ]
        })
        
        st.session_state.messages.append({
            "type": "ai",
            "content": [
                "Great, now explain to me your target demographic.",
            ]
        })
    
    st.chat_input(key="chat_input", on_submit=_)

if len(st.session_state.messages) == 3:
    def _():
        st.session_state.messages.append({
            "type": "user",
            "content": [
                st.session_state.chat_input,
            ]
        })
        
        st.session_state.messages.append({
            "type": "ai",
            "content": [
                "Sounds good!",
                "Now I will try to parse the target demographic, hang on."
            ]
        })
    
    st.chat_input(key="chat_input", on_submit=_)

if len(st.session_state.messages) == 5:
    pd = st.session_state.messages[1]["content"][0]
    td = st.session_state.messages[3]["content"][0]
    
    parsed_demographic = parse_demographic(pd, td)
    
    st.session_state.messages.append({
        "type": "ai",
        "content": [
            "Here is the demographic I could identify from your input.",
            f"**Age:** From {parsed_demographic.minage} to {parsed_demographic.maxage} years old",
            f"**Gender:** {'No specific gender' if parsed_demographic.gender == 'null' else parsed_demographic.gender.capitalize()}",
            f"**Religion:** {'No specific religion' if parsed_demographic.religion == 'null' else parsed_demographic.religion.capitalize()}",
            f"**Occupations:** {', '.join(parsed_demographic.occupations) if len(parsed_demographic.occupations) > 0 else "No specific occupation"}",
            f"**Lifestyle:** {parsed_demographic.lifestyle if parsed_demographic.lifestyle else 'No specific lifestyle'}",
            f"**Interests:** {', '.join(parsed_demographic.interests) if len(parsed_demographic.interests) > 0 else "No specific interests"}",
        ]
    })
    st.session_state.parsed_demographic = parsed_demographic
    
    st.rerun()

if len(st.session_state.messages) == 6:
    st.session_state.messages.append({
        "type": "ai",
        "content": [
            "Now I will generate an audience persona using the above demographic. It might take a minute.",
        ]
    })
    
    st.rerun()

if len(st.session_state.messages) == 7:
    pd = st.session_state.messages[1]["content"][0]
    parsed_demographic = st.session_state.parsed_demographic
    
    persona = generate_persona(pd, parsed_demographic)
    
    st.session_state.messages.append({
        "type": "ai",
        "content": [
            "### Personal Information",
            f"**Name:** {persona.name}",
            f"**Age:** {persona.age} Years",
            f"**Job:** {persona.job}",
            f"**Location:** {persona.location}",
            f"**Education:** {persona.education}",
            "### Background",
            persona.background,
            "### Personality",
            *persona.personality,
            "### Goals",
            *persona.goals,
            "### Frustrations",
            *persona.frustrations,
        ]
    })
    
    st.session_state.persona = persona
    
    st.rerun()
