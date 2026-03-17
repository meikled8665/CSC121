import requests
import openmeteo_requests

import pandas as pd

def getWeather(city):
    openmeteo = openmeteo_requests.Client()
    
    #gets the location
    locationUrl = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response1 = requests.get(locationUrl, headers = {"User-Agent" : "My App"})
    response1 = response1.json()
    
    Params = {
        "latitude" : response1[0]["lat"],
        "longitude" : response1[0]["lon"],
        "hourly" : "temperature_2m"
    }
    
    #actually getting the weather
    weatherUrl = "https://api.open-meteo.com/v1/forecast"
    responses = openmeteo.weather_api(weatherUrl, params = Params)
    
    response2 = responses[0]
    hourly = response2.Hourly()
    hourly_temperature_2m = hourly.Variables(0).ValuesAsNumpy()
    
    hourly_data = {"date": pd.date_range(
	start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
	end =  pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
	freq = pd.Timedelta(seconds = hourly.Interval()),
	inclusive = "left"
    )}
    
    hourly_data["temperature_2m"] = hourly_temperature_2m
    
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    #print("\nHourly data\n", hourly_dataframe)
    
    temperature = hourly_dataframe[hourly_dataframe.last_valid_index][2]
    
    return temperature



def getPokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url) #will be a json
    
    if response.status_code == 404:
        print(f"{name} not found.")
        exit()
    else:
        pass
    
    response = response.json()
    
    pokeType = response["types"][0]["type"]["name"]
    weight = response["weight"]
    
    return pokeType, weight


def main():
    pokeName = input("Enter the name of a pokemon: ").lower()
    pokeType, pokeWeight = getPokemon(pokeName)
    
    city = input("Enter a city and state(seperate with a comma): ")
    temperature = getWeather(city)
    
    print(f"{pokeName} is a/an {pokeType} type and weighs {pokeWeight}lbs")
    print(f"{pokeName} is in {city} and it is currently {temperature}°C")

if __name__ == "__main__":
    main()