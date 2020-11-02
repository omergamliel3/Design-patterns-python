# Observer pattern weather station example

import requests
from secrets import API_ENDPOINT, API_KEY
from observer_pattern import ObservableInterface, ObserverInterface

CITY_NAME = 'LONDON'

# Implement concrete observable, as WeatherStation
class WeatherStation(ObservableInterface):
    def __init__(self, city:str):
        # maintains all observers
        self.observers = []
        # the current weather state
        self.weather_state = str
        # the current weather state desc
        self.weather_state_description = str
        # the current city name
        self.city = city

    # add observer to observers list
    def add(self, observer: ObserverInterface):
        self.observers.append(observer)

    # remove observer to observers list
    def remove(self, observer: ObserverInterface):
        self.observers.remove(observer)

    # notify all observers
    def notify(self):
        for observer in self.observers:
            observer.update()

    # assign new state and notify observers
    def emit(self, state: str, description: str):
        self.weather_state = state
        self.weather_state_description = description
        self.notify()

    # return the current weather state and description
    def getWeather(self):
        return self.city ,self.weather_state, self.weather_state_description
    
    # fetch weather from weather api
    def fetchWeather(self):
        try:
            # make http get requests
            response = requests.get(f'{API_ENDPOINT}/weather?q={self.city}&appid={API_KEY}')
            # handle bad response
            if response.ok == False:
                print('Bad request. Message:' ,response.json()['message'])
                return
            # extract weather data from response 
            weather_main = response.json()['weather'][0]['main']
            weather_description = response.json()['weather'][0]['description']
            # emits new weather state
            self.emit(weather_main, weather_description)
        except requests.HTTPError as err:
            print(f'http error:\t{err}')
        


# Implement concrete observer, as Display
class Display(ObserverInterface):
    def __init__(self, observable: WeatherStation):
        self.subject = observable
        self.city: str
        self.weather = str
        self.description = str

    # get weather state from subject and show the current weather
    def update(self):
        self.city, self.weather, self.description = self.subject.getWeather()
        self.showWeather()
    
    # show the current weather state
    def showWeather(self):
         print(f'Display {self.city} weather: {self.weather}')
         print(f'Weather info: {self.description}')

    
# takes a city string input and returns the input
def getCityInput():
    while True:
        try:
            city = input('ENTER CITY NAME FOR WEATHER INFORMATION: ')
            return city
        except:
            print('YOU MUST ENTER A VALID CITY NAME')
            continue
        

# main 
def main():
    city_name = getCityInput()
    # create an observable
    weather_station = WeatherStation(city_name)
    # create a display observer
    display = Display(weather_station)
    # add display observer to weather_station observers
    weather_station.add(display)
    # fetching weather
    weather_station.fetchWeather()


if __name__ == "__main__":
    main()