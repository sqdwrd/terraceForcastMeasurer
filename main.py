class Dht11Data:
    def __init__(self, temp: int, humidity: int):
        self.temp = temp
        self.humidity = humidity


def main():
    dht11_measurement = measure()
    write(dht11_measurement)


def measure() -> Dht11Data:
    raise NotImplementedError


def write(dht11: Dht11Data):
    raise NotImplementedError


if __name__ == '__main__':
    main()
