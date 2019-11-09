import csv
from datetime import timezone, datetime
from time import sleep

import pandas as pd
import requests

from weather_thief.personal_data_live import secret_key, longitude, latitude


def call_api(time):
    url = f'https://api.darksky.net/forecast/{secret_key}/{latitude},{longitude},{time}'

    response = requests.get(url)

    if response.status_code == 200:
        print('Success!')
    else:
        print('Oh noes! it died')
        print(response.status_code)
        return {"hourly": {'data': []}}
    return response.json()


def time_loop(open_file):
    for year in range(2019, 2020):
        for month in range(9, 13):
            for day in range(1, 32):
                try:
                    dt = datetime(year=year, month=month, day=day, hour=23)
                    time = int(dt.replace(tzinfo=timezone.utc).timestamp())
                    json_response = call_api(time)
                    df_weather = pd.DataFrame.from_records(json_response['hourly']['data'])
                    df_weather.to_csv(open_file, header=False, quoting=csv.QUOTE_NONE)
                    sleep(0.25)
                except ValueError:
                    continue


def get_data():
    with open('weather_data.csv', mode='a') as csv_file:
        time_loop(csv_file)


def analyze_this():
    data_input = pd.read_csv('weather_data.csv')
    print(data_input.to_string())


# get_data()
analyze_this()
