import requests


def get_coordinates(city):
    try:    
        url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
        response = requests.get(url)
        data = response.json()

        for i, place in enumerate(data["results"]):
            print(i, place["name"], place["admin1"], place["country"])
        
        choice = int(input(f"Choose number for {city} specific weather to pull: "))
        lat = data["results"][choice]["latitude"]
        lon = data["results"][choice]["longitude"]
        return lat, lon
        
    except (KeyError,IndexError,ValueError):
        print("Invalid City/Option. Please check spelling and try again.")
        return None, None
    
def get_temperature(lat, lon):
    try:
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m&temperature_unit=fahrenheit"
        response = requests.get(url)
        data = response.json()
        return data["current"]["temperature_2m"]
    except (requests.exceptions.ConnectionError, KeyError):
        print("We ran into a Connection Error")
        return None