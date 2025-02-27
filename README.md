# 🌍 AI-Powered Travel Planner

## Overview
The **AI Powered Travel Planner** is a smart travel assistant that helps users find the best travel options  two locations. It utilizes AI to provide recommendations for flights, trains, buses, and cabs, considering factors such as distance, estimated travel time, and cost.

## Features
- **AI Powered recommendations** - Provides travel options with estimated travel time and costs.
- **Multiple Modes of Transport** -  Suggests flights, trains, buses, and cabs.
- **Detailed Travel Insights** - Highlights key details such as layovers, stops, and budget-friendly options.
- **User-Friendly Interface** - Built using Streamlit for a smooth experience

## How It Works
1. User enters **Source** and **Destination** cities.
2. Selects the **Travel Date** and **Number of Passengers**.
3. Clicks **Find Travel Options** to get AI-powered recommendations.
4. The system fetches travel details and presents them in a structured format.
5. Users can explore **additional insights** for better decision-making

## Tech Stack
- Python
- Streamlit
- Langchain
- Google Gemini AI


## Steup Instructions
1. **Clone the Repository**
```
git clone <repository-url>
cd <repository-folder>
```
2. **Install Dependencies**
```
pip install -r requirements.txt
```
3. **Create a .env file:** Add your Google API key to the .env file.
```
GOOGLE_API_KEY=your_google_api_key_here
```
4. **Run the Streamlit app:** After installing the required libraries and setting up the .env file, run the app using:
```
streamlit run app1.py
```
