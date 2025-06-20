import streamlit as st
from outfit_planner import generate_outfit
from rag_retriever import get_cultural_tips
import subprocess

st.set_page_config(page_title="ThreadTrek AI", layout="centered")
st.title("🧵👟 ThreadTrek AI – Travel-Ready Outfit Planner")

destination = st.text_input("Where are you traveling to?")
activity = st.selectbox("What’s your main activity?", ["Beach", "Trekking", "Business", "Temple Visit", "City Tour"])
weather = st.selectbox("Expected weather?", ["Hot", "Cold", "Rainy", "Mild"])

if destination and activity and weather:
    st.subheader("🧳 Outfit Suggestion:")
    outfit = generate_outfit(destination, activity, weather)
    st.success(outfit)

    st.subheader("📚 Cultural Dressing Tips:")
    tips = get_cultural_tips(destination)
    st.markdown(tips)

    st.subheader("📸 OOTD Instagram Caption:")
    caption_prompt = f"Create a travel outfit Instagram caption for a trip to {destination} while doing {activity} in {weather} weather."
    result = subprocess.run(["ollama", "run", "tinyllama", caption_prompt], capture_output=True, text=True)
    st.text_area("Generated Caption:", result.stdout.strip(), height=150)
