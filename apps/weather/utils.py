import requests

def get_weather_data(city):
    # URL и параметры запроса к API погоды
    url = f"https://api.weatherapi.com/v1/forecast.json?key=becb7890982a45ccb32110018241807&q={city}&days=7&aqi=no&alerts=no"
    response = requests.get(url)
    if response.status_code != 200:
        return False, response.status_code
    return normalize_json(response.json()), response.status_code


def normalize_json(weather_json):
    returning_json = {}
    returning_json['city'] = f"{weather_json['location']['name']}, {weather_json['location']['country']}"
    returning_json['current_weather'] = weather_json['current']['temp_c']
    returning_json['current_condition'] = weather_json['current']['condition']['text']
    dates = []
    for i in range(7):
        dates.append({
            "date":weather_json['forecast']['forecastday'][i]['date'],
            "from":weather_json['forecast']['forecastday'][i]['day']['mintemp_c'],
            "to":weather_json['forecast']['forecastday'][i]['day']['maxtemp_c'],
            "condition":weather_json['forecast']['forecastday'][i]['day']['condition']['text']
            })
    returning_json['dates'] = dates
    return returning_json
