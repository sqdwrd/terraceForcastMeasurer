from pathlib import Path


class WeatherData:
    def __init__(self, temp: float, humidity: float):
        self.temp = temp
        self.humidity = humidity

    def toStrList(self) -> list[str]:
        return [str(self.temp), str(self.humidity)]


class Paths:
    home = Path.home()
    data = home.joinpath("forecast")
    measure = data.joinpath("measure.csv")
    forecast = data.joinpath("forecast.csv")

    def __init__(self):
        if not self.data.exists():
            self.data.mkdir()
