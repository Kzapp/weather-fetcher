import requests
import os
import csv 
from datetime import datetime

fieldnames = ["date", "city", "temperature"]

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
    except requests.exceptions.ConnectionError:
        print("We ran into a Connection Error")
        return None
    

def log_weather(city,temp):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")    
    if os.path.exists("weather_log.csv"):
        with open("weather_log.csv", "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["date", "city", "temperature"])
            writer.writerow({"date": now, "city": city,"temperature": temp})
    else:
        with open ("weather_log.csv", "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow({"date": now, "city": city,"temperature": temp})


while True:
    city = input("Enter City: ")
    lat, lon = get_coordinates(city)
    if lat is None:
        print("Could not get weather - Inavlid City.")
    else:    
        temp = get_temperature(lat, lon)
        if temp is None:
            print("Could not get weather - Connection Error.")
            answer = input("Would you like the search another city? (Y/N): ")
            if answer.lower() == "n":
                break

        else:    
            print(f"The current temperature in {city} is {temp} °F")
            log_weather(city, temp)
            answer = input("Would you like the search another city? (Y/N): ")
            if answer.lower() == "n":
                print("GoodBye!")
                break