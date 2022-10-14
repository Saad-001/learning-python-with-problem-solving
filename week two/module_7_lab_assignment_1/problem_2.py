"""
2. Use web search to find some API to get weather data. Use that to get your region’s weather data every 30 minute.

Write a function named weather_data() and write your code inside this function.

"""
import json
import time

import requests
import schedule

import creds

weather_api = f"https://api.openweathermap.org/data/2.5/weather?lat={creds.latitude}&lon={creds.longitude}&appid={creds.api_key}"

def weather_data() :
    response = requests.get(weather_api)
    content = response.content.decode("UTF-8")
    main_content = json.loads(content)
    
    print(main_content)

schedule.every(30).minutes.do(weather_data)

while True:
    schedule.run_pending()
    time.sleep(5)

