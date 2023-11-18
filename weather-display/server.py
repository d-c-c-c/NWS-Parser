from flask import Flask
from flask_cors import CORS

#Files from current project
from xmlparser import organize
import weathericons
import forecast
from weathericons import current_weather_code
from forecast import daily_data
from datetime import datetime
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/data')
def data():
    xmlData = organize()
    time = datetime.now()
    icon = weathericons.checkIfNight(time.hour, weathericons.iconMatch(current_weather_code))
    # Returning an api for showing in  reactjs
    return {
        "Location":xmlData['Location'],
        "TempF":xmlData['TempF'],
        "TempC":xmlData['TempC'],
        "Weather":xmlData['Weather'],
        "Zipcode":"23666",
        "Humidity":xmlData['Humidity'],
        "Wind_Direction":xmlData['Wind Direction'],
        "Wind_Speed":xmlData['Wind Speed'],
        "Dew_Point":xmlData['Dew Point'],
        "Visibility":xmlData['Visibility'],
        "Icon": icon
        }

@app.route('/data/forecast')
def forecastData():
    weather_codes = forecast.trimDecimals(daily_data['weather_code'].tolist())
    temp_max = forecast.formatDecimals(daily_data['temperature_2m_max'].tolist(), 1)
    temp_min = forecast.formatDecimals(daily_data['temperature_2m_min'].tolist(), 1)
    wind_max = forecast.formatDecimals(daily_data['wind_speed_10m_max'].tolist(), 1)
    return {
        "Weather_Codes": weather_codes,
        "Temp_Max": temp_max,
        "Temp_Min": temp_min,
        "Wind_Max": wind_max
    }
 
     
# Running app
if __name__ == '__main__':
    app.run()
    