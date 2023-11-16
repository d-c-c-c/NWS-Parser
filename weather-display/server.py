from flask import Flask
from flask_cors import CORS
from xmlparser import organize
import datetime
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/data')
def data():
    time = datetime.datetime.now()
    xmlData = organize()
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
        "Date": time
        }

 
     
# Running app
if __name__ == '__main__':
    app.run()