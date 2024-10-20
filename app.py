from flask import Flask, render_template, jsonify
import requests
import pandas as pd
from datetime import datetime
import time

app = Flask(__name__)

API_KEY = 'YOUR API KEY'
CITIES = ['Delhi', 'Mumbai', 'Chennai', 'Bangalore', 'Kolkata', 'Hyderabad']
INTERVAL = 1 

# Helper function to convert Kelvin to Celsius
def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

# Function to get weather data for a specific city
def get_weather_data(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            'city': city,
            'temp': kelvin_to_celsius(data['main']['temp']),
            'feels_like': kelvin_to_celsius(data['main']['feels_like']),
            'main': data['weather'][0]['main'],
            'timestamp': data['dt']
        }
    return None

# Route to render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch weather data
@app.route('/weather')
def weather():
    weather_data = []
    for city in CITIES:
        data = get_weather_data(city)
        if data:
            weather_data.append(data)
    return jsonify(weather_data)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)
