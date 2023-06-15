from datetime import datetime
from pathlib import Path


class WeatherData:
    def __init__(self, temp: float, humidity: float, timestamp: int = None):
        if timestamp is None:
            timestamp = datetime.now().timestamp()

        self.timestamp = timestamp
        self.temp = temp
        self.humidity = humidity

    def toStrList(self) -> list[str]:
        from zoneinfo import ZoneInfo
        return [datetime.fromtimestamp(self.timestamp, tz=ZoneInfo("Asia/Seoul")).strftime("%Y-%m-%d %H:%M:%S"),
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
