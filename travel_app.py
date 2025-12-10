# travel_app.py

import streamlit as st
import os
from dotenv import load_dotenv
import groq

# Load API key
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

client = groq.Client(api_key=api_key)

def ask_travel_bot(question):
    system_prompt = """
    You are a professional travel planner AI.
    Give a simple, clear 1-day itinerary in bullet points.
    Include places, food, budget, and tips.
    """
    chat = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    )
    return chat.choices[0].message.content

# Page setup
st.set_page_config(page_title="Travel Planner Bot", page_icon="🌍", layout="centered")

# 🎨 FULL PAGE BACKGROUND COLOR (Sky Blue)
st.markdown("""
<style>
html, body, .stApp {
    background-color: #E3F2FD !important;  /* FULL PAGE Sky Blue */
    height: 100%;
    margin: 0;
    padding: 0;
}

.itinerary-box {
    background-color: rgba(255, 255, 255, 0.96);
    color: #000000;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #90CAF9;
    box-shadow: 8px 8px 20px rgba(0,0,0,0.12);
    margin-top: 20px;
}

h2 {
    color: #1565C0;
    margin-bottom: 15px;
    font-weight: 700;
}
</style>
""", unsafe_allow_html=True)

# UI (same as your original)
st.title("🌏 Travel Planner Bot")
st.write("Get a *1-Day Travel Plan* for any city!")

city = st.text_input("Enter the city for your trip:")
budget_level = st.selectbox("Choose your budget level:", ["Low", "Medium", "High"])

if st.button("Plan My Trip"):
    if city:
        question = f"Plan a 1-day trip in {city} for a {budget_level.lower()} budget student."
        with st.spinner("Generating itinerary..."):
            itinerary = ask_travel_bot(question)

        st.markdown(
            f'<div class="itinerary-box"><h2>Itinerary for {city}</h2><p>{itinerary.replace("\\n", "<br>")}</p></div>',
            unsafe_allow_html=True
        )
    else:
        st.warning("Please enter a city!")