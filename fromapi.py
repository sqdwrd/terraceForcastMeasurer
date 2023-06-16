import csv

import requests
import pathlib
import xml.etree.ElementTree as ElemTree
from globals import *


def readKey() -> str:
    key_path = pathlib.Path(__file__).parent.resolve().joinpath("weather.credential")
    with key_path.open("r") as file:
        return file.read()


def getApi() -> requests.Response:
    auth_key = readKey()
    api_url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={auth_key}&numOfRows=1000&pageNo=1&base_date=20230616&base_time=0500&nx=55&ny=127"

    return requests.get(api_url)


def parse(response: requests.Response) -> WeatherData:
    tree = ElemTree.fromstring(response.text)
    items = tree.findall(".//item")

    temp = humidity = None
    weather = None

    seconds_from_date = (int(items[0].find("fcstTime").text) / 100) * 3600
    date = datetime.fromtimestamp(
        datetime.strptime(items[0].find("fcstDate").text, "%Y%m%d").timestamp() + seconds_from_date)

    for item in items:
        category = item.find("category")

        def getValue():
            return float(item.find("fcstValue").text)

        if category.text == "TMP":
            temp = getValue()
        elif category.text == "REH":
            humidity = getValue()

        if temp is not None and humidity is not None:
            weather = WeatherData(temp, humidity, date)

    if weather is None:
        if temp is None:
            temp = -1
        if humidity is None:
            humidity = -1

        weather = WeatherData(temp, humidity, date)

    return weather


def write(weather: WeatherData):
    forecast_file = Paths.forecast.open("a+")
    forecast_csv = csv.writer(forecast_file)
    forecast_csv.writerow(weather.toStrList())


def main():
    api_result = getApi()
    weather = parse(api_result)
    write(weather)


if __name__ == '__main__':
    main()
