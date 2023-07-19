##Check if the ISS satellite is above my house then send me an email to look at the sky

import requests
from datetime import datetime

MY_LAT = -1.343154
MY_LONG = -48.454308
url = "https://api.sunrise-sunset.org/json"

parameters = {"lat":MY_LAT,"lng":MY_LONG,"formatted":0}
time_now = datetime.now()
print(time_now.hour)
#print(type(parameters["lat"]))
try:
    response = requests.get(url=url,params=parameters)
    response.raise_for_status()

    data = response.json()


except requests.exceptions.RequestException as e:
    print("Error occurred:", e)


iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

#TODO 1: Get the ISS current  position


#TODO 2: Create a function to return True or False if my position is within +5 or -5 degrees of the ISS position

#TODO 3: Create a function to send me an email

#TODO 4: Check If the ISS is close to my current position and it is currently dark

#TODO 5: Create a while loop to run the code every 60 seconds.



