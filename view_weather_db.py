import sqlite3
from datetime import datetime

def log_weather(city, temp):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_log (
            date TEXT,
            city TEXT,
            temperature REAL                     
        )
    """)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("""
        INSERT INTO weather_log (date, city, temperature)           
        VALUES (?, ?, ?)           
    """, (now, city, temp))

    conn.commit()
    conn.close()


conn = sqlite3.connect("weather.db")
cursor = conn.cursor()
cursor.execute("SELECT * FROM weather_log")
rows = cursor.fetchall()
for row in rows:
    date, city, temp = row
    print(f"{date} - {city} - {temp} °F")
conn.close()