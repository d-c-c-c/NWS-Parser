import "./current-weather.css"
import React, { useState, useEffect } from "react";
const CurrentWeather = () => {
    // usestate for setting a javascript
    // object for storing and using data
    const [data, setdata] = useState({
        location:"",
        temp_f:0,
        temp_c:0,
        weather:"",
        zipcode:"",
        humidity:"",
        dew_point:"",
        wind_dir:"",
        wind_speed:0,
        visibility:"",
    });

    //Used to keep track of the current time (UTC)
    //Could be changed to local time with ___.toLocaleString()
    const [date, setDate] = useState(new Date().toLocaleString());

    useEffect(() => {
        //Update the time displayed every second
        let curTime = setInterval(() => {
            setDate(new Date().toLocaleString())
        }, 1000)

        return () => clearInterval(curTime);
    }, []);

    
   
    

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
                    temp_f:data.TempF,
                    temp_c:data.TempC,
                    weather:data.Weather,
                    zipcode:data.Zipcode,
                    humidity:data.Humidity,
                    wind_dir:data.Wind_Direction,
                    wind_speed:data.Wind_Speed,
                    dew_point:data.Dew_Point,
                    visibility:data.Visibility,
                });
            })
        );
    });
    return (
        <div className = "weatherContainer">
            <div className = "weatherHeader">
                <p className = "locationName">Current Weather at {data.location}</p>
                <p className = "currentTime" id ="currentTime">{date}</p>
            
            </div>
            <div className ="weatherInfo">
                <img alt = "weather" className = "weather-icon" src="icons/01d.png" />
                <div className = "tempDiv">
                    <p className = "temperature">{data.temp_f}°F</p>
                    <p className = "temperature">{data.temp_c}°C</p>
                </div>
                <div className = "details">
                    <p className="param-row">
                        <span className = "param-details">Dew Point:</span>
                        <span className = "param-value">{data.dew_point}</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Wind Speed:</span>
                        <span className = "param-value">{data.wind_dir} {data.wind_speed} MPH</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Relative Humidity</span>
                        <span className = "param-value">{data.humidity} %</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Visibility:</span>
                        <span className = "param-value">{data.visibility} mi</span>
                    </p>
                </div>
                            
            </div>
            <div className = "weatherFooter">
                <span className = "weather-description">{data.weather}</span>
                <a href="https://forecast.weather.gov/MapClick.php?lat=38.91788999499656&lon=-77.53821002204819" target="_blank" rel="noopener noreferrer">More Details</a>
            </div>
        </div>
    );
}




export default CurrentWeather;