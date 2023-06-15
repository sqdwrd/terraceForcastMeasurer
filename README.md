# terraceForecastMeasurer
김천고등학교 88기 3학년 테라스 프로젝트의 일부

* 파이썬과 라즈베리파이를 통해 DHT11 온습도 센서 데이터 기록
* 기상청 API 데이터 저장
* crontab을 통해 자동화

### 데이터 구조(CSV)
`~/.forecast/measurement.csv`에 저장

| 시간(yyyy-MM-dd HH:mm:ss) | 온도(섭씨) | 습도(%) |
|-------------------------|--------|-------|
