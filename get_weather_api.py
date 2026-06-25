from flask import Flask, request
from get_longitude_and_latitude import get_lon_lat
from get_weather_details import get_weather

app = Flask(__name__)

@app.route("/get-weather", methods=["POST"])   #Routes our endpoint to http://localhost:5000/
def print_weather():
    weather_str = ""
    json_dict = request.get_json()
    lon_lat = get_lon_lat(json_dict["postcodes"])   #Get the postcodes from the request
    if len(lon_lat) > 0:  # Checks that there are correct zip codes
        for postcode in lon_lat.keys():  # Gets postcodes from the dictionary while looping
            weather_details = get_weather(lon_lat[postcode][0], lon_lat[postcode][1], postcode)
            name, postcode, temp, feels_like, desc = weather_details
            weather_str += f"Today's weather forecast in {name}, specifically {postcode}: \nTemperature: {temp}\nFeels like: {feels_like}\nDescription: {desc}\n\n"
    else:
        return "These postcodes are not valid"
    return weather_str

if __name__ == "__main__":  #Will run only if this file is run
    app.run(debug=True)
