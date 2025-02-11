const url = "https://wttr.in";

// Input and button
const submitBtn = document.querySelector("#submit-btn");
const inputCity = document.querySelector("#city-input");

// Error div
const errorDiv = document.querySelector("#error");

// City and temperature div
const cityDiv = document.querySelector("#city");
const temperatureDiv = document.querySelector("#temp");

// div for min and max
const minTempDiv = document.querySelector("#minTemp");
const maxTempDiv = document.querySelector("#maxTemp");

// div for humidity
const humidityDiv = document.querySelector("#humidity");

// div for feelsLike
const feelsLikeDiv = document.querySelector("#feelsLike");


submitBtn.addEventListener("click", (event) => {
    setValues(inputCity.value);
});

function clearAll() {
    cityDiv.innerHTML = '-';
    temperatureDiv.innerHTML = "-";
    humidityDiv.innerHTML = "-";
    cityDiv.innerHTML = '-';
    temperatureDiv.innerHTML = `-`;
    minTempDiv.innerHTML = `-`;
    maxTempDiv.innerHTML = `-`;
}


async function setValues(city) {
    errorDiv.style.display = "none";

    try {
        let response = await fetch(`${url}/$${city}?format=j1`);
        console.log(response);
        
        if (!response.ok) {
            showErrorDiv();
            clearAll();
            errorDiv.innerHTML = "Please enter valid city name";
            return; 
        }
        response = await response.json();

        city = response?.nearest_area[0]?.areaName[0]?.value;

        // If city is undefined
        if (!city) {
            showErrorDiv();
            clearAll();
            errorDiv.innerHTML = "City not found, please type correct name"; 
            return;
        }
        
        // Set city name
        cityDiv.innerHTML = city;

        // extract temperature
        let temperature = response?.current_condition[0]?.temp_C;
        
        if (!temperature) {
            showErrorDiv();
            clearAll();
            errorDiv.innerHTML = "Couldn't retrieve temperature"; 
            return;
        }
        
        const weather = response?.weather;
        // Set temperature
        temperatureDiv.innerHTML = `${temperature}&deg;C`;

        // Get Max and Min temperature
        let minTemp = Infinity, maxTemp = -Infinity;
    
        
        weather.forEach((element) => {
            minTemp = Math.min(minTemp, parseInt(element.mintempC));
            maxTemp = Math.max(maxTemp, parseInt(element.maxtempC));
        });
        
        if (!minTemp || !maxTemp) {
            showErrorDiv();
            errorDiv.innerHTML = "Min and Max is not defined";
            clearAll();
            return;
        }

        // set min and max temperature
        minTempDiv.innerHTML = `${minTemp}&deg;C`;
        maxTempDiv.innerHTML = `${maxTemp}&deg;C`;

        const humidity = response.current_condition[0]?.humidity;
        
        if (!humidity) {
            showErrorDiv();
            clearAll();
            return;
        }
        
        // Set value of humidity
        humidityDiv.innerHTML = humidity;
        
        const feelsLike = response.current_condition[0].FeelsLikeC; 
        if (!feelsLike) {
            showErrorDiv();
            errorDiv.innerHTML = "Couldn't fetch feels like &deg;C";
            clearAll();
            return;
        }

        feelsLikeDiv.innerHTML = feelsLike;
    } catch (error) {
        
        showErrorDiv();
        clearAll();
        console.log(error?.message);
        errorDiv.innerHTML = `Something went wrong from server side`
    }
}


function showErrorDiv() {
    errorDiv.style.display = "block";
}