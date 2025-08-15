import sys
import os

# --- This is our guaranteed fix ---
# It adds the project's root directory to Python's path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# ------------------------------------

from app.api import get_futurama_characters
from app.mongo_db_storage import store_characters_in_mongodb 

def main():
    """Main function to run the data fetching and storing process."""
    print("Starting the application...")
    
    character_data = get_futurama_characters()
    
    if character_data:
        store_characters_in_mongodb(character_data)
    else:
        print("Failed to fetch character data. Nothing to store.")
        
    print("Application finished.")

if __name__ == "__main__":
    main()