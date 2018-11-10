import math
from typing import Union


class Angle:
    symbol: str

    def __init__(self, angle: Union[str, int, float]):
        self._angle: Union[str, int, float] = float(angle)

    @property
    def angle(self) -> float:
        return self._angle

    @angle.setter
    def angle(self, angle: float):
        self._angle = angle

    def all(self) -> dict:
        options = {**self.as_degrees, **self.as_radians, **self.as_gradians}

        # Removes the angle which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def as_degrees(self) -> dict:
        return {"deg": self._angle}

    @property
    def as_radians(self) -> dict:
        return {"rad": self._angle}

    @property
    def as_gradians(self) -> dict:
        return {"grad": self._angle}


class Degree(Angle):
    symbol = "deg"

    @property
    def as_radians(self) -> dict:
        angle = self._angle * math.pi / 180

        return {"rad": angle}

    @property
    def as_gradians(self) -> dict:
        angle = self._angle * 200/180

        return {"grad": angle}


class Radian(Angle):
    symbol = "rad"

    @property
    def as_degrees(self) -> dict:
        angle = self._angle * 180 / math.pi

        return {"deg": angle}

    @property
    def as_gradians(self) -> dict:
        angle = self._angle * 200 / math.pi

        return {"grad": angle}


class Gradian(Angle):
    symbol = "grad"

    @property
    def as_degrees(self) -> dict:
        angle = self._angle * 180 / 200

        return {"deg": angle}

    @property
    def as_radians(self) -> dict:
        angle = self._angle * math.pi / 200

        return {"rad": angle}
