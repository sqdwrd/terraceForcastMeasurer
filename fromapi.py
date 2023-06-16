import csv

import requests
import pathlib
import xml.etree.ElementTree as ElemTree
from globals import *


def readKey() -> str:
    key_path = pathlib.Path(__file__).parent.resolve().joinpath("weather.credential")
    with key_path.open("r") as file:
        return file.read()


def getApi(base_time: datetime, key: str) -> requests.Response:
    if base_time.hour % 3 != 2:
        raise ValueError(f"Invalid hour, value was:{base_time.hour}")

    api_url = f"http://apis.data.go.kr/1360000/VilageFcstInfoService_2.0/getVilageFcst?serviceKey={key}&numOfRows=1000&pageNo=1&base_date={base_time.strftime('%Y%m%d')}&base_time={base_time.strftime('%H')}00&nx=55&ny=127"
    print(f"fromapi.getApi: getting {api_url}")
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
    def latestUpdateHour(base_hour: int) -> int:
        """기상청 단기예보의 API 요청에 맞게 base_hour로부터 가장 최근의 기준시(02, 05, 08, ..., 23) 반환"""
        if base_hour % 3 != 2:
            return (base_hour // 3) * 3 + 2

    def latestUpdateTime(base_time: datetime) -> datetime:
        return base_time.replace(hour=latestUpdateHour(base_time.hour), minute=0, second=0, microsecond=0)

    base_time = latestUpdateTime(datetime.now())
    print(f"fromapi.main: base_time is {base_time}")
    api_result = getApi(base_time, key=readKey())

    weather = parse(api_result)
    write(weather)


if __name__ == '__main__':
    main()
