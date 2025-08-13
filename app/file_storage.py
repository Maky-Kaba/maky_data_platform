import os
import json

def store_character_files(character_data):
    """Saves each character's data into a separate JSON file."""
    # Ensure the output directory exists
    output_dir = "output/characters"
    os.makedirs(output_dir, exist_ok=True)

    if not character_data:
        print("No character data to store.")
        return

    for character in character_data:
        # Use the character's ID for the filename
        file_path = os.path.join(output_dir, f"{character['id']}.json")
        with open(file_path, "w", encoding='utf-8') as f:
            # Write the JSON data with nice formatting
            json.dump(character, f, indent=2)
    
    print(f"Saved character data to the '{output_dir}' directory.")