# terraceForecastMeasurer

김천고등학교 88기 3학년 테라스 프로젝트의 일부

* 파이썬과 라즈베리파이를 통해 DHT11 온습도 센서 데이터 기록
* 기상청 API 데이터 저장
* crontab을 통해 자동화

## 데이터 구조(CSV)

`~/.forecast/measurement.csv`에 저장

| 시간(yyyy-MM-dd HH:mm:ss)(KST) | 온도(섭씨) | 습도(%) |
|------------------------------|--------|-------|

## 기상청 API 정보

* https://www.data.go.kr/data/15084084/openapi.do 의 기상청 단기예보 API 활용
* XML 파일을 기반으로 전송됨
* 2시, 5시, 8시 ...의 3시간 주기로 업데이트되며, API 제공은 업데이트 후 10분 후부터 제공
* 3시간마다 데이터를 받아 와서, 24시간 후의 온습도 데이터를 저장

### 구현

* 프로젝트의 `/weather.credential` 파일에 기록된 API 인증키(encoded)를 읽어 `requests.get()`