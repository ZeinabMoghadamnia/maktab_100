import requests

class Weather:
    def __init__(self, city_name, api_key):
        self.city_name = city_name
        self.api_key = api_key
        
    def get_weather_data(self):
        '''get url and informations and check its successfull or not'''
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={self.city_name}&appid={self.api_key}"

            with requests.get(url) as response:
                response.raise_for_status()
                data = response.json()
                current_temperature_kelvin = data["main"]["temp"]
                current_temperature_celsius = current_temperature_kelvin - 273.15

                return round(current_temperature_celsius, 1)
        except requests.exceptions.RequestException as e:
            return f"Error connecting to the service: {e}"
        except KeyError:
            return "Error in received data!"

temp = Weather("Tehran","1d23b5fc6043031715d16d21264a529a")
temperature = temp.get_weather_data()
if isinstance(temperature, float):
    print(f"Temperature in {temp.city_name} is {temperature} C.")
else:
    print(temperature)
