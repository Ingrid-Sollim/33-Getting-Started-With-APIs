##Check if the ISS satellite is above my house then send me an email to look at the sky

import requests
from datetime import datetime
from config import *
import time

MY_LAT = -50.0091
MY_LONG = 124.9855
url = "https://api.sunrise-sunset.org/json"

parameters = {"lat":MY_LAT,"lng":MY_LONG,"formatted":0}

try:
    response = requests.get(url=url,params=parameters)
    response.raise_for_status()

    data = response.json()


except requests.exceptions.RequestException as e:
    print("Error occurred:", e)

sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
# print(sunrise)
# print(sunset)
time_now = datetime.now().hour

#TODO 1: Get the ISS current  position
#Created in the config file

#TODO 2: Create a function to return True or False if my position is within +5 or -5 degrees of the ISS position
#Created in the config file
#TODO 3: Create a function to send me an email
msg = "Loop Up. The ISS is above your head"
receiver = "ingridsollim@hotmail.com"
#Created in the config file



#TODO 5: Create a while loop to run the code every 60 seconds.
while True:
    #TODO 4: Check If the ISS is close to my current position and it is currently dark
    iss_lat,iss_long = get_iss_position()
    if my_position_and_iss(MY_LAT,MY_LONG,iss_lat,iss_long) and sunrise>time_now>=sunset:
        email_sender(msg, receiver)
        print("Email sent")
        break
    else:
        print("The ISS is far away from my home")

    time.sleep(60)

