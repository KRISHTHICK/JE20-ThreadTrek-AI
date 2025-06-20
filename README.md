# JE20-ThreadTrek-AI
GenAI

🧵👟 ThreadTrek AI – AI-Powered Travel Outfit Planner
🎯 Concept:
ThreadTrek AI helps users plan outfits for travel based on destination, weather, activities, and cultural etiquette. It uses RAG (Retrieval-Augmented Generation) to fetch destination-specific fashion norms and combines them with AI-generated outfit suggestions, powered locally with Ollama, Python, and Streamlit.

🌟 Key Features:
Feature	Description
📍 Destination-Based Styling	Suggests outfits suitable for a destination based on culture & climate
🌡️ Weather-Ready Recommendations	Pulls local weather (mock or API) for smart outfit layering
🧳 Activity-Based Wardrobe Packs	Choose trip activities (trek, beach, formal) and receive full outfit packs
📚 RAG-Enhanced Cultural Guide	Pulls info on local dress codes (temples, cities) and blends into suggestions
📸 OOTD Caption Generator	Generates social captions for trip pictures using Ollama

# 🧵👟 ThreadTrek AI – AI-Powered Travel Outfit Planner

Plan your travel wardrobe with AI based on destination, activity, and weather — plus cultural tips using RAG.

## ✨ Features
- Destination-aware outfit suggestions
- Weather and activity-based planning
- Cultural dress code guide (RAG)
- Instagram caption generator using Ollama

## 🚀 How to Run Locally

```bash
git clone https://github.com/yourusername/ThreadTrek-AI.git
cd ThreadTrek-AI
pip install -r requirements.txt
ollama run tinyllama
streamlit run app.py

