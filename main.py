# We import the specific functions we need from our modules
from app.api import get_futurama_characters
from app.file_storage import store_character_files

def main():
    """Main function to run the data fetching and storing process."""
    print("Starting the application...")
    character_data = get_futurama_characters()
    
    # Only try to store data if the API call was successful
    if character_data:
        store_character_files(character_data)
        
    print("Application finished.")

# This is a standard Python construct
if __name__ == "__main__":
    main()