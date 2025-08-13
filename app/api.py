import requests

def get_futurama_characters():
    """Fetches character data from the Futurama API."""
    url = "https://distansakademin.github.io/api/futurama/characters"
    
    try:
        response = requests.get(url)
        # This will raise an error for bad responses (4xx or 5xx)
        response.raise_for_status() 
        data = response.json()
        print(f"Fetched {len(data)} characters from the API.")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from API: {e}")
        return None