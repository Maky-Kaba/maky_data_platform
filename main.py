import sys
import os

# --- This is our guaranteed fix ---
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
# ------------------------------------

from app.api import get_futurama_characters
from app.mongo_db_storage import store_characters_in_mongodb
from app.mysql_storage import store_characters_in_mysql  # <-- NEW LINE
from app.s3_storage import upload_to_s3 # <-- NEW LINE

def main():
    """Main function to fetch data and store it in multiple databases."""
    print("Starting the application...")
    
    # 1. Fetch character data from the API
    character_data = get_futurama_characters()
    
    if character_data:
        # 2. Store the data in MongoDB
        store_characters_in_mongodb(character_data)
        
        # 3. Store the same data in MySQL
        store_characters_in_mysql(character_data) # <-- NEW LINE
    else:
        print("Failed to fetch character data. Nothing to store.")


     # --- Phase 2: IoT Sensor Data ---
    print("\n--- Starting S3 Upload ---")
    bucket_name = "makyfirst"  # <-- IMPORTANT: REPLACE THIS
    local_file = "data/sensor_data.json"
    s3_file_name = "iot-data/sensor_data.json" # Store it in a "folder" in S3
    
    upload_to_s3(local_file, bucket_name, s3_file_name)
        
    print("Application finished.")

if __name__ == "__main__":
    main()