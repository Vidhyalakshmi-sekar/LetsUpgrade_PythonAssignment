import requests
from datetime import datetime
my_weather_api_key = ''     # enter your own weather api key

city_name = input('Please enter your city name: ')
# Weather API call
weather_api_link = ' https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(city_name, my_weather_api_key)
api_link = requests.get(weather_api_link)
api_data = api_link.json()

# if the cod response is 404, the city name does not exist

if api_data['cod'] == '404':
    print('Invalid city: {}, please enter a valid city name.'.format(city_name))
else:
    # converting kelvin unit to celsius by subtracting kelvin value by 273.15
    temperature = api_data['main']['temp'] - 273.15
    temperature = '{:.2f}'.format(temperature)
    weather_description = (api_data['weather'][0]['description']).capitalize()
    humidity = api_data['main']['humidity']
    # converting wind speed from m/sec to km/hr
    wind_speed = '{:.2f}'.format(api_data['wind']['speed'] * 3.6)
    country = api_data['sys']['country']
    date_time = datetime.now().strftime('%d-%B-%Y, %I:%M:%S %p')

    print('--------------------------------------------------------------------------------------------')
    print('The weather report for {}, {} at {}'.format(city_name, country, date_time))
    print('--------------------------------------------------------------------------------------------')

    print('Temperature         : {} °C'.format(temperature))
    print('Weather Description : {}'.format(weather_description))
    print('Humidity            : {} %'.format(humidity))
    print('Wind Speed          : {} km/hr'.format(wind_speed))
