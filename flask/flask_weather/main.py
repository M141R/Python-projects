from flask import Flask, render_template, request

import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    location : str
    description : str
    temp_c : float  

app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def weatherapp():
    weather_data = None

    if request.method == 'POST': 
        city = request.form['CityName']
        weather_data = main(city)
        print(weather_data)
        
    return render_template('index.html', weather = weather_data or {})


# @app.route('/weather')
def weather(city_name, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city_name
    }
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print(f"API request failed with status code {response.status_code}")
        return None

    json_response = response.json()

    if json_response is None:
        print("API response is not valid JSON")
        return None

    weather_data = WeatherData(
        location = json_response.get("location").get("name"),
        description = json_response.get("current").get("condition").get("text"),
        temp_c = json_response.get("current").get("temp_c")
    )

    return weather_data
def main(city_name):
    weather_data = weather(city_name,api_key)
    return weather_data

print(weather(api_key,'London'))

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug= "True")


# https://pastebin.com/Ge9YwFJt : Weather Images
    
