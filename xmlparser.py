from flask import Flask
from flask_cors import CORS
import datetime
 
time = datetime.datetime.now()
 
# Initializing flask app
app = Flask(__name__)
CORS(app)
 
# Route for seeing a data
@app.route('/data')
def get_time():
 
    # Returning an api for showing in  reactjs
    return {
        'Name':"Test", 
        "Age":"22",
        "Date":time, 
        "programming":"python"
        }
 
     
# Running app
if __name__ == '__main__':
    app.run()