class Observer:
    def update(self, temperature, humidity, pressure):
        pass

class WeatherStation:
    def __init__(self):
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    def weather_data(self, temperature, humidity, pressure):
        for observer in self.observers:
            observer.update(temperature,humidity, pressure)

class DisplayDevice(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f"{self.name} Display")
        print(f" - Temperature: {temperature}C, Humidity: {humidity}%, Pressure: {pressure} hPa")


class WeatherApp(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f"{self.name} App - Weather Update")
        print(f" - Temperature: {temperature} C, Humidity: {humidity}%, Pressure: {pressure} hPa")

def main():
    weather_station = WeatherStation()

    display1 = DisplayDevice("living room")
    display2 = DisplayDevice("Kitchen")
    app1 = WeatherApp("Mobile App")

    weather_station.add_observer(display1)
    weather_station.add_observer(display2)
    weather_station.add_observer(app1)

    weather_station.weather_data(25.5, 60, 1013.2)
    weather_station.weather_data(26.0, 58, 1112.8)

if __name__ == "__main__":
    main()