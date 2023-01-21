import openai
import streamlit as st
import os

openai.api_key = st.secrets["api_key"]

def generate_bio(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

st.set_page_config(page_title="Dating App Bio Generator", page_icon=":couple:", layout="wide")

st.title("Dating App Bio Generator")

name = st.text_input("What is your name?")
age = st.number_input("What is your age?", min_value=18, max_value=99)
location = st.text_input("What is your location?")
hobbies = st.text_input("What are your hobbies?")

prompt = (f"Please write a dating app bio for a {age} year old named {name} from {location} who enjoys {hobbies}. Make it flirty.")


bio = generate_bio(prompt)

st.write("Here is your generated bio:")
st.write(bio)
