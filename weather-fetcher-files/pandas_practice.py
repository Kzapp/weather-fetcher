import pandas as pd
import sqlite3

conn = sqlite3.connect("weather.db")
df = pd.read_sql_query("SELECT * FROM weather_log", conn)
print(df)
print(df["temperature"])
print(df["date"])

