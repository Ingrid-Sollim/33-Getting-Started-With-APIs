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
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    print(sunrise.split("T")[1].split(":")[0])
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)