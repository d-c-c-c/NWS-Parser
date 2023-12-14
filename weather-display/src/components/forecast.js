import "../styles/forecast.css"
import React, { useState, useEffect } from "react";

const Forecast = () => {

    const [data, setdata] = useState({
        days:[],
        weather_codes:[],
        temp_max:[],
        temp_min:[],
        wind_max:[]
    });

    useEffect(() => {
        //using setInterval to limit the number of GET requests sent to the server
        const interval = setInterval(() => {
      
        fetch("/data/forecast").then((res) =>
            res.json().then((data) => {
                // Setting data from API
                // value MUST match the name given in the JSON string; Case Sensitive
                setdata({
                    days:data.Days,
                    weather_codes:data.Weather_Codes,
                    temp_max:data.Temp_Max,
                    temp_min:data.Temp_Min,
                    wind_max:data.Wind_Max
                });
            })
        );
        }, 2000) 
        return () => {clearInterval(interval)};
    }, []);
    //List of days used for the forecast list
    return (
        <div>
            <span className = "forecast-header">10 Day Forecast</span>
            <div className = "forecastWrapper">
                <div className = "forecastContainer">
                    
                    {data.days.map((day, index) => (

                        <div className = "forecast-item-container">
                            <li key = {index} id = {index} className = "forecast-list">{day}</li>
                            <img alt = "weather" className = "forecast-weather-icon" src={`icons/${data.weather_codes[index][0]}.png`} />
                            <div className = "forecastDetails">
                            <p className="param-row">
                                <span className = "param-details">Temperature Hi: </span>
                                <span className = "param-value">{data.temp_max[index]} °F</span>
                            </p>
                            <p className="param-row">
                                <span className = "param-details">Temperature Lo: </span>
                                <span className = "param-value">{data.temp_min[index]} °F</span>
                            </p>
                            <p className="param-row">
                                <span className = "param-details">Wind Speed: </span>
                                <span className = "param-value">{data.wind_max[index]} MPH</span>
                            </p>
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default Forecast