import smtplib
import requests

#TODO 1: Create function to send email
MY_EMAIL="***********"
PASSWORD="****"

def email_sender(message, email_receiver):
    '''Inform the message to be sent and the person's email address to send an automatic email'''

    global MY_EMAIL,PASSWORD
    email_msg = f"Subject: ISS Location Status\n\n{message}"
    try:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,to_addrs=email_receiver, msg=email_msg)
    except:
        print("Connection fail")

#TODO 2: Get the ISS current  position


def get_iss_position():
    '''This function returns a tuple with the ISS latitude and longitude'''
    url="http://api.open-notify.org/iss-now.json"
    response = requests.get(url=url)
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    location_iss = (latitude,longitude)
    print(location_iss)
    return location_iss

#iss_lat,iss_long = get_iss_postion()
#TODO 3: Create a function to return True or False if my position is within +5 or -5 degrees of the ISS position


def my_position_and_iss(my_lat,my_long,iss_lat,iss_long):
    ''' Returns True if the location provided is in the ISS range and False if is not'''
    if (my_lat + 5 > iss_lat > my_lat - 5) and (my_long + 5 > iss_long > my_long - 5):
        return True
    else:
        return False

#print(f"{MY_LAT + 5},{MY_LONG - 5}")
# if my_position_and_iss(MY_LAT,MY_LONG,iss_lat,iss_long):
#     print("Look up")
#
# else:
#     print("Far away")
