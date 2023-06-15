import csv
from pathlib import Path
from datetime import datetime

path_home = Path.home()
path_data = path_home.joinpath("forecast")
path_measure = path_data.joinpath("measure.csv")

if not path_data.exists():
    path_data.mkdir()


class Dht11Data:
    def __init__(self, temp: float, humidity: float):
        self.temp = temp
        self.humidity = humidity

    def toStrList(self) -> list[str]:
        return [str(self.temp), str(self.humidity)]


def measure() -> Dht11Data:
    raise NotImplementedError


def write(dht11: Dht11Data):
    if not path_measure.exists():
        path_measure.touch()
    measure_file = path_measure.open("a+")
    measure_csv = csv.writer(measure_file)

    measure_csv.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S")] + dht11.toStrList())

    measure_file.close()


def main():
    dht11_measurement = measure()
    write(dht11_measurement)


def test_write():
    write(Dht11Data(25, 40))
    write(Dht11Data(30.5, 60.5))
