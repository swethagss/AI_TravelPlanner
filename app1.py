import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(model='gemini-2.0-flash-exp', google_api_key=GOOGLE_API_KEY)

system_prompt = """
You are an intelligent travel assistant that provides users with the best travel recommendations.
For a given source and destination, calculate the approximate distance and suggest travel options, including flights, trains, buses, and cabs.
Each option should have estimated travel time, cost, and key details such as stops or layovers.
Focus on reliability, affordability, and user convenience while presenting the data in a well-organized manner.
"""

prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{query}")
])

output_parser = StrOutputParser()

# Streamlit UI
st.set_page_config(page_title='AI Travel Planner')
st.title("🧳 AI-Powered Travel Planner")

col1, col2 = st.columns(2)
with col1:
    source = st.text_input("🌍 Source", placeholder="Enter departure city")
with col2:
    destination = st.text_input("📍 Destination", placeholder="Enter destination city")

date = st.date_input('📅 Travel Date')
passengers = st.number_input("👥 Number of Passengers", min_value=1, value=1)

# Language selection with more options
languages = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Chinese": "zh",
    "Japanese": "ja",
    "Korean": "ko",
    "Hindi": "hi",
    "Arabic": "ar",
    "Portuguese": "pt",
    "Russian": "ru",
    "Telugu" : "te",
    "Tamil" : "ta",
    "Kannada" : "kn",
    "Malayalam" : "ml"
}

selected_lang = st.selectbox("🌍 Select Language", list(languages.keys()))

if st.button("🔍 Find Travel Options"):
    if not source or not destination:
        st.warning("⚠️ Please enter both source and destination!")
    else:
        user_query = f"Provide travel options for {source} to {destination} on {date} for {passengers} passengers in {selected_lang} language."
        
        chain = prompt_template | model | output_parser
        response = chain.invoke({"query": user_query})

        st.subheader("✈️🚆🚌 Travel Options")
        
        # Formatting headings
        st.markdown("""
    <style>
        .travel-heading {
            font-weight: bold;
            font-size: 28px;  /* Increased font size */
            padding: 8px;
            display: block;
        }
        .flight { color: red; }
        .train { color: blue; }
        .bus { color: green; }
        .cab { color: orange; }  /* Fixed CAB issue */
    </style>
""", unsafe_allow_html=True)

        
        formatted_response = response.replace("Flight:", "<span class='travel-heading flight'>✈️ Flight:</span>") \
                             .replace("Train:", "<span class='travel-heading train'>🚆 Train:</span>") \
                             .replace("Bus:", "<span class='travel-heading bus'>🚌 Bus:</span>") \
                             .replace("Cab/Self-Drive:", "<span class='travel-heading cab'>🚖 Cab/Self-Drive:</span>")

        
        st.markdown(formatted_response, unsafe_allow_html=True)