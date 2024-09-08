import requests 
from dotenv import load_dotenv
import os 
from pprint import pprint

load_dotenv()

def get_current_weather(city="New York"):
    # print('\n*** Get Current Weather Conditions ***\n')

    # city = input("\nPlease enter a city name:\n")
    
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric' 
# "&q" = query parameters
    # print(request_url)

    weather_data = requests.get(request_url).json()

    # pprint(f'\nCurrent Weather for {weather_data["name"]}') #dict index?
    # pprint(f'\nThe temp is {weather_data["main"]["temp"]}')
    # pprint(f'\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.')

    pprint(weather_data)
    return weather_data


    
# &q - query


if __name__ == "__main__":
    print('\n*** Get Current Weather Conditions ***\n')

    city = input("\nPlease enter a city name: ")

    # check for empty strings or string with only spaces
    if not bool(city.strip()): 
        city = "Manila"

    weather_data = get_current_weather(city)

    pprint(weather_data)
    # pprint(weather_data)
    # get_current_weather(city)
    
