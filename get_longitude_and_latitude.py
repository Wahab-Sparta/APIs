import requests

def get_lon_lat(postcodes):
    lon_lat = {}
    POSTCODE_ENDPOINT = "https://api.postcodes.io/postcodes/"   #Postcode Endpoint + headers + body for the POST request
    headers = {"Content-Type": "application/json"}
    body = {"postcodes": postcodes}
    data = requests.post(url=POSTCODE_ENDPOINT, headers=headers, json=body).json()  #POST request
    count = 0   #Need this to loop through the data
    for postcode in postcodes:  #loops through the postcodes
        if data["result"][count]["result"]:    #Checking to see if the postcode exists
            response = data["result"][count]["result"]  # Getting result
            longitude, latitude = response["longitude"], response["latitude"] #Getting longitude & latitude
            lon_lat[postcode] = [longitude, latitude]
        else:
            print(f"{postcode} is not a postcode.\n")    #Will print this if the postcode doesn't exist
        count += 1
    return(lon_lat)