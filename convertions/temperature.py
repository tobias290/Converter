from typing import Union


class Temperature:
    symbol: str

    def __init__(self, temp: Union[str, int, float]):
        self._temp: Union[str, int, float] = float(temp)

    @property
    def temperature(self) -> float:
        return self._temp

    @temperature.setter
    def temperature(self, temp: float):
        self._temp = temp

    def all(self) -> dict:
        options = {**self.as_celsius, **self.as_fahrenheit, **self.as_kelvin}

        # Removes the temperature which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def as_celsius(self) -> dict:
        return {"°C": self._temp}

    @property
    def as_fahrenheit(self) -> dict:
        return {"°F": self._temp}

    @property
    def as_kelvin(self) -> dict:
        return {"K": self._temp}


class Celsius(Temperature):
    symbol = "°C"

    @property
    def as_fahrenheit(self) -> dict:
        temp = (self._temp * 9 / 5) + 32

        return {"°F": temp}

    @property
    def as_kelvin(self) -> dict:
        temp = self._temp + 273.15

        return {"K": temp}


class Fahrenheit(Temperature):
    symbol = "°F"

    @property
    def as_celsius(self) -> dict:
        temp = (self._temp - 32) * 5 / 9

        return {"°C": temp}

    @property
    def as_kelvin(self) -> dict:
        temp = self._temp * 5 / 9 + 273.15

        return {"K": temp}


class Kelvin(Temperature):
    symbol = "K"

    @property
    def as_celsius(self) -> dict:
        temp = self._temp - 273.15

        return {"°C": temp}

    @property
    def as_fahrenheit(self) -> dict:
        temp = (self._temp - 273.15) * 9 / 5 + 32

        return {"°F": temp}
