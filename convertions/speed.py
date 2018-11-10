from typing import Union


class Speed:
    symbol: str

    def __init__(self, speed: Union[int, float]):
        self._speed = float(speed)

    @property
    def speed(self) -> float:
        return self._speed

    @speed.setter
    def speed(self, speed: Union[int, float]):
        self._speed = speed

    def all(self) -> dict:
        options = {
            **self.as_miles_per_hours,
            **self.as_kilometres_per_hour,
            **self.as_knots,
            **self.as_metres_per_second,
        }

        # Removes the angle which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def as_miles_per_hours(self) -> dict:
        return {"mph": self._speed}

    @property
    def as_kilometres_per_hour(self) -> dict:
        return {"kph": self._speed}

    @property
    def as_knots(self) -> dict:
        return {"knots": self._speed}

    @property
    def as_metres_per_second(self) -> dict:
        return {"mps": self._speed}


class MilesPerHour(Speed):
    symbol = "mph"

    @property
    def as_kilometres_per_hour(self) -> dict:
        speed = self._speed * 1.609

        return {"kph": speed}

    @property
    def as_knots(self) -> dict:
        speed = self._speed / 1.151

        return {"knots": speed}

    @property
    def as_metres_per_second(self) -> dict:
        speed = self._speed / 2.237

        return {"mps": speed}


class KilometresPerHour(Speed):
    symbol = "kph"

    @property
    def as_miles_per_hours(self) -> dict:
        speed = self._speed / 1.609

        return {"mph": speed}

    @property
    def as_knots(self) -> dict:
        speed = self._speed / 1.852

        return {"knots": speed}

    @property
    def as_metres_per_second(self) -> dict:
        speed = self._speed / 3.6

        return {"mps": speed}


class Knot(Speed):
    symbol = "knots"

    @property
    def as_miles_per_hours(self) -> dict:
        speed = self._speed * 1.151

        return {"mph": speed}

    @property
    def as_kilometres_per_hour(self) -> dict:
        speed = self._speed * 1.852

        return {"kph": speed}

    @property
    def as_metres_per_second(self) -> dict:
        speed = self._speed / 1.944

        return {"mps": speed}


class MetersPerSecond(Speed):
    symbol = "mps"

    @property
    def as_miles_per_hours(self) -> dict:
        speed = self._speed * 2.237

        return {"mph": speed}

    @property
    def as_kilometres_per_hour(self) -> dict:
        speed = self._speed * 3.6

        return {"kph": speed}

    @property
    def as_knots(self) -> dict:
        speed = self._speed * 1.944

        return {"knots": speed}
