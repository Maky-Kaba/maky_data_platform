from pymongo import MongoClient

def store_characters_in_mongodb(character_data):
    if not character_data:
        print("No character data to store in MongoDB.")
        return

    client = MongoClient("mongodb://localhost:1337")
    db = client["futurama"]
    collection = db["characters"]
    collection.delete_many({})
    collection.insert_many(character_data)
    
    print(f"Saved {len(character_data)} characters to MongoDB in the 'futurama.characters' collection.")
    
    client.close()