import os
import json
from flask import Flask

app = Flask(__name__)

def get_character_names():
    """Reads all JSON files and returns a list of character names."""
    character_names = []
    data_dir = "output/characters"
    if not os.path.exists(data_dir):
        return ["No character data found. Please run main.py first."]
    
    for filename in os.listdir(data_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(data_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                # Assumes the name is stored like: {'name': {'first': 'Philip', 'last': 'Fry'}}
                full_name = f"{data['name']['first']} {data['name']['last']}"
                character_names.append(full_name)
    return character_names

@app.route('/')
def home():
    names = get_character_names()
    # Start building the HTML response
    html = "<h1>Futurama Characters</h1>"
    html += "<ul>" # Start an unordered list
    for name in names:
        html += f"<li>{name}</li>" # Add each name as a list item
    html += "</ul>" # Close the list
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)