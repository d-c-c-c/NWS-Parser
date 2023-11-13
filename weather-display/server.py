from flask import Flask
from flask_cors import CORS
from xmlparser import organize
import datetime
 
time = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/data')
def data():
    xmlData = organize()
    # Returning an api for showing in  reactjs
    return {
        "Location":xmlData['Location'],
        "Temperature":xmlData['Temperature'],
        "Weather":xmlData['Weather'],
        "Zipcode":"23666"
        }

 
     
# Running app
if __name__ == '__main__':
    app.run()