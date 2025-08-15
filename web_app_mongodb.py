from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

def get_character_names_from_db():
    """Connects to MongoDB and retrieves a list of character names."""
    try:
        # Establish a connection to the MongoDB container
        client = MongoClient("mongodb://localhost:1337", serverSelectionTimeoutMS=5000)
        db = client["futurama"]
        collection = db["characters"]
        
        # Find all documents, but only return the 'name' field
        # The second argument to find() is a "projection"
        # We sort by the character ID to ensure a consistent order
        characters = collection.find({}, {"_id": 0, "name": 1}).sort("id")
        
        names = [f"{char['name']['first']} {char['name']['last']}" for char in characters]
        
        client.close()
        return names
    except Exception as e:
        # If the database is down, return an informative error message
        print(f"Error connecting to MongoDB: {e}")
        return ["Error: Could not connect to the database."]

@app.route('/')
def home():
    """Renders the home page with a list of character names."""
    names = get_character_names_from_db()
    
    # Build the HTML response string
    html = "<h1>Futurama Characters (from MongoDB)</h1>"
    html += "<ul>"
    for name in names:
        html += f"<li>{name}</li>"
    html += "</ul>"
    
    return html

if __name__ == '__main__':
    # The standard port for Cloud Shell web preview is 8080
    app.run(host='0.0.0.0', port=8080, debug=True)