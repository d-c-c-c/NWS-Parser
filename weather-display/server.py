from flask import Flask
from flask_cors import CORS

#Files from current project
from xmlparser import organize
import weathericons
from weathericons import current_weather_code
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

 
     
# Running app
if __name__ == '__main__':
    app.run()
    