import csv
from datetime import datetime

from globals import *

if not Paths.data.exists():
    Paths.data.mkdir()


def measure() -> WeatherData:
    raise NotImplementedError


def write(dht11: WeatherData):
    if not Paths.measure.exists():
        Paths.measure.touch()
    measure_file = Paths.measure.open("a+")
    measure_csv = csv.writer(measure_file)

    measure_csv.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S")] + dht11.toStrList())

    measure_file.close()


def main():
    dht11_measurement = measure()
    write(dht11_measurement)


def test_write():
    write(WeatherData(25, 40))
    write(WeatherData(30.5, 60.5))
