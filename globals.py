from datetime import datetime
from pathlib import Path


class WeatherData:
    def __init__(self, temp: float, humidity: float, timestamp: datetime = None):
        if timestamp is None:
            timestamp = datetime.now()

        from zoneinfo import ZoneInfo
        self.timestamp = datetime.fromtimestamp(timestamp.timestamp(), tz=ZoneInfo("Asia/Seoul"))

        self.temp = temp
        self.humidity = humidity

    def toStrList(self) -> list[str]:
        return [self.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                str(self.temp),
                str(self.humidity)]


class Paths:
    home = Path.home()
    data = home.joinpath("forecast")
    measure = data.joinpath("measure.csv")
    forecast = data.joinpath("forecast.csv")

    def __init__(self):
        if not self.data.exists():
            self.data.mkdir()
