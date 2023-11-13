import "./current-weather.css"
import React, { useState, useEffect } from "react";
const CurrentWeather = () => {
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
        <div className = "weatherContainer">
            <div className = "weatherHeader">Current Weather at {data.location}</div>
            <div className ="weatherInfo">
                <img alt = "weather" className = "weather-icon" src="icons/01d.png" />
                <p className = "temperature">{data.temperature}</p>
                <div className = "details">
                    <p className="param-row">
                        <span className = "param-details">Wind Speed: 1000</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Wind Speed: 1000</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Wind Speed: 1000</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Wind Speed: 1000</span>
                    </p>
                </div>
                            
            </div>
            <div className = "weatherFooter">
                <span className = "weather-description">{data.weather}</span>
                <a href="FILLER">More Details</a>
            </div>
        </div>
    );
}

export default CurrentWeather;