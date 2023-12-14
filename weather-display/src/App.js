import CurrentWeather from './components/current-weather'; 
import Forecast from './components/forecast';
import Search from './components/search';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <div className = "current-weather-component">
        <CurrentWeather />
        </div>
        <div className = "forecast-component">
          <Forecast />
        </div>
        
      </header>
    </div>
  );
}

export default App;
