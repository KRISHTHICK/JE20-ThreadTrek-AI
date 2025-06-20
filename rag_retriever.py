import json
import os

def get_cultural_tips(destination):
    try:
        with open("assets/locations.json", "r") as file:
            data = json.load(file)
        return data.get(destination.lower(), "No specific cultural tips found for this destination.")
    except:
        return "⚠️ Could not load cultural tips. Make sure `locations.json` is present."
