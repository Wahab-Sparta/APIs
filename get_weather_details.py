import requests

def get_weather(longitude, latitude, postcode):
    WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"    #Weather endpoint
    with open("weather_api_key") as file:   #Getting my API key from a file
        api_key = file.readline().strip()
    data = requests.get(WEATHER_ENDPOINT + f"?lat={latitude}&lon={longitude}&appid={api_key}&units=metric").json()  #Gets weather data
    name, temp, feels_like, desc = data["name"], data["main"]["temp"], data["main"]["feels_like"], data["weather"][0]["description"]
    return [name, postcode, temp, feels_like, desc]