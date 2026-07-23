import os
import csv 
from datetime import datetime

fieldnames = ["date", "city", "temperature"]


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