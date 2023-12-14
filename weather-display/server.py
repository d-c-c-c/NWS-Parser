from flask import Flask
from flask_cors import CORS

#Files from current project
from xmlparser import organize
import weathericons
import forecast
from weathericons import current_weather_code
from forecast import daily_data, hourly_data, wind_bearing, temperature_c, visibility_mi
from datetime import datetime
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/data')
def data():
    xmlData = organize()
    time = datetime.now()
    # Tuple of the weather icon code and weather code
    weatherCodeInfo = weathericons.iconMatch(current_weather_code)
    icon = weathericons.checkIfNight(time.hour, weatherCodeInfo[0])
    # Returning an api for showing in  reactjs
    return {
        "Location":"Hampton, VA (Placeholder)",
        "TempF":str((round(hourly_data["temperature_2m"][0], 1))),
        "TempC":str((round(temperature_c[0], 1))),
        "Weather":weatherCodeInfo[1],
        "Zipcode":"23666",
        "Humidity":str((round(hourly_data["relative_humidity_2m"][0], 1))),
        "Wind_Direction": wind_bearing[0],
        "Wind_Speed":str((round(hourly_data["wind_speed_10m"][0], 1))),
        "Dew_Point":str((round(hourly_data["dew_point_2m"][0], 1))),
        "Visibility":str((round(visibility_mi[0], 1))),
        "Icon": icon
        }

@app.route('/data/forecast')
def forecastData():
    time = datetime.now()
    forecast_weather_codes = forecast.trimDecimals(daily_data['weather_code'].tolist())

    #Changing date timestamps into their corresponding days
    forecast_days = daily_data['date'].strftime("%A").tolist()
    #Turning weather codes into their corresponding icons
    for i in range(len(forecast_weather_codes)):
        forecast_weather_codes[i] = weathericons.iconMatch(forecast_weather_codes[i])

    temp_max = forecast.formatDecimals(daily_data['temperature_2m_max'].tolist(), 1)
    temp_min = forecast.formatDecimals(daily_data['temperature_2m_min'].tolist(), 1)
    wind_max = forecast.formatDecimals(daily_data['wind_speed_10m_max'].tolist(), 1)
    return {
        "Days": forecast_days,
        "Weather_Codes": forecast_weather_codes,
        "Temp_Max": temp_max,
        "Temp_Min": temp_min,
        "Wind_Max": wind_max
    }
 
     
# Running app
if __name__ == '__main__':
    app.run()
    