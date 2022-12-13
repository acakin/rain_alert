import requests
from twilio.rest import Client

api_key = "***"
account_sid = "***"
auth_token = "***"

LAT = 39.77
LON = 30.53


parameters = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key
}

response = requests.get("http://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
data = response.json()
twelve_hours = []
for _ in range(0,4):
    twelve_hours.append(data["list"][_]["weather"][0]["main"])
if "Rain" in twelve_hours:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="Don't forget to take an ☔.",
        from_='+1***',
        to='+90***'
    )

    print(message.status)

