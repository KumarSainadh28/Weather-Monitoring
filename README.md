# Weather-Monitoring

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Folder Structure](#folder-structure)

## Overview
The **Real-Time Weather Monitoring System** is a Flask-based web application that fetches and displays current weather data for multiple Indian cities. The application utilizes the OpenWeatherMap API to provide real-time weather updates, including temperature, feels-like temperature, weather conditions, and timestamps.

## Features
- Displays current weather data for selected cities.
- User-friendly and attractive UI for easy navigation.
- Fetches real-time weather updates every few minutes.
- Provides temperature in Celsius with weather conditions.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS
- **API**: OpenWeatherMap API
- **Data Handling**: Pandas

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/KumarSainadh28/Weather-Monitoring.git
   cd Weather-Monitoring
## Create a virtual environment
 ```bash
      python -m venv venv
```
## Activate the Virtual Environment
Windows:
   ```bash
   venv\Scripts\activate
```
## Install the required packages
```bash
pip install -r requirements.txt

```
## Usage
1.Ensure your OpenWeatherMap API key is correctly set in the app.py file.
2.Run the application
```bash
python app.py
```
3.Open your web browser and navigate to http://127.0.0.1:8000/ to view the weather data.

## Folder Structure

WeatherMonitoringSystem/
```bash
├── app.py                # Main application file
├── templates/            # HTML templates folder
│   └── index.html       # Main HTML template
├── static/               # Static files folder (CSS)
│   └── styles.css       # CSS styles
└── requirements.txt      # List of required packages
```
