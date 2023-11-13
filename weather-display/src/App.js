import React, { useState, useEffect } from "react";
import logo from './logo.svg';
import './App.css';

function App() {
  // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
      location:"",
      temperature:"",
      weather:"",
      zipcode:""
  });

  // Using useEffect for single rendering
  useEffect(() => {
      // Using fetch to fetch the api from 
      // flask server it will be redirected to proxy
      fetch("/data").then((res) =>
          res.json().then((data) => {
              // Setting data from API
              // value MUST match the name given in the JSON string; Case Sensitive
              setdata({
                  location:data.Location,
                  temperature:data.Temperature,
                  weather:data.Weather,
                  zipcode:data.Zipcode
              });
          })
      );
  });
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <h1>React and flask</h1>
                {/* Calling data to display */}
                <p>{data.location}</p>
                <p>{data.temperature}</p>
                <p>{data.weather}</p>
                <p>{data.zipcode}</p>
      </header>
    </div>
  );
}

export default App;
