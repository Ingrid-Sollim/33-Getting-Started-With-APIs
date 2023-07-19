import requests
MY_LAT = -1.343154
MY_LONG = -48.454308
url = "https://api.sunrise-sunset.org/json?"

parameters = {"lat":MY_LAT,"lng":MY_LONG}
#print(type(parameters["lat"]))
try:
    response = requests.get(url=url,params=parameters)
    response.raise_for_status()

    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error occurred:", e)