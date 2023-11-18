import "../styles/forecast.css"
import React, { useState, useEffect } from "react";

const Forecast = () => {

    //List of days used for the forecast list
    const days = ["Monday","Tuesday","Wednesday","Thursday","Friday"];
    return (

        <div className = "forecastContainer">

            {days.map((day, index) => (

                <div className = "forecast-item-container">
                    <li key = {index} id = {index}>{day}</li>
                    <img alt = "weather" className = "forecast-weather-icon" src={`icons/unknown.png`} />
                    <div className = "forecastDetails">
                    <p className="param-row">
                        <span className = "param-details">Dew Point:</span>
                        <span className = "param-value">1000</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Dew Point:</span>
                        <span className = "param-value">1000</span>
                    </p>
                    <p className="param-row">
                        <span className = "param-details">Dew Point:</span>
                        <span className = "param-value">1000</span>
                    </p>
                    </div>
                </div>
            ))}
        </div>
    )
}

export default Forecast