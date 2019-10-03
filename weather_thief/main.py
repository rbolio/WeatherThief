import requests
import csv
from datetime import timezone, datetime
from weather_thief.personal_data_live import secret_key, longitude, latitude


def call_api(time):
    url = f'https://api.darksky.net/forecast/{secret_key}/{latitude},{longitude},{time}'

    response = requests.get(url)

    if response.status_code == 200:
        print('Success!')
    else:
        print('We broke it')
        exit(0)
    return response.json()


def time_loop():

    for year in range(2017, 2020):
        for month in range(1, 13):
            for day in range(1, 32):
                try:
                    dt = datetime(year=year, month=month, day=day, hour=12)
                    time = int(dt.replace(tzinfo=timezone.utc).timestamp())
                    info_json = call_api(time)
                    #write info json
                except ValueError:
                    continue






def append_to_csv(input_json):
    for hourly_data in input_json['hourly']['data']:
        time = hourly_data['time']
        temperature = hourly_data['temperature']
        print(f'Hour:{time}, temperature: {temperature}')


dt = datetime(year=2018, month=12, day=5, hour=23)
time = int(dt.replace(tzinfo=timezone.utc).timestamp())
json_response = call_api(time)

