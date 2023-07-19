import requests
url="http://api.open-notify.org/iss-now.json"
response = requests.get(url=url)
response.raise_for_status()

data = response.json()
data_keys=data.keys()
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
location = (latitude,longitude)
print(location)