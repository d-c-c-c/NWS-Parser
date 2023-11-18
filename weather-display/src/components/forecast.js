import "../styles/forecast.css"
import React, { useState, useEffect } from "react";

const Forecast = () => {

    //List of days used for the forecast list
    const days = ["Monday","Tuesday","Wednesday","Thursday","Friday"];
    return (

        <div className = "forecastContainer">

            {days.map((day, index) => (

                <div className = "forecast-item-container">
                    <li key = {index}>{day}</li>
                    <img alt = "weather" className = "forecast-weather-icon" src={`icons/unknown.png`} />
                    <label>Test</label>
                </div>
            ))}
        </div>
    )
}

export default Forecast