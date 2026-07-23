from weather_api import get_coordinates, get_temperature
from weather_db import log_weather


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