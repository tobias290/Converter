# NOTE: Different type of Tonne may have been used
from typing import Union


class Weight:
    symbol: str

    def __init__(self, weight: Union[str, int, float]):
        self._weight: Union[str, int, float] = float(weight)

    def all(self) -> dict:
        options = {
            **self.as_grams,
            **self.as_kilograms,
            **self.as_pounds,
            **self.as_ounces,
            **self.as_tonnes,
            **self.as_stone,
        }

        # Removes the weight which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float):
        self._weight = weight

    @property
    def as_pounds(self) -> dict:
        return {"lb": self._weight}

    @property
    def as_ounces(self) -> dict:
        return {"oz": self._weight}

    @property
    def as_grams(self) -> dict:
        return {"g": self._weight}

    @property
    def as_kilograms(self) -> dict:
        return {"kg": self._weight}

    @property
    def as_tonnes(self) -> dict:
        return {"T": self._weight}

    @property
    def as_stone(self) -> dict:
        return {"st": self._weight}


class Kilogram(Weight):
    symbol = "kg"

    @property
    def as_pounds(self) -> dict:
        weight = self._weight / 0.45359237

        return {"lb": weight}

    @property
    def as_ounces(self) -> dict:
        weight = self._weight / 0.02834952

        return {"oz": weight}

    @property
    def as_grams(self) -> dict:
        weight = self._weight * 1000

        return {"g": weight}

    @property
    def as_tonnes(self) -> dict:
        weight = self._weight / 1000

        return {"T": weight}

    @property
    def as_stone(self) -> dict:
        weight = self._weight * 0.15747

        return {"st": weight}


class Gram(Weight):
    symbol = "g"

    @property
    def as_pounds(self) -> dict:
        weight = self._weight / 453.59237

        return {"lb": weight}

    @property
    def as_ounces(self) -> dict:
        weight = self._weight / 28.34952

        return {"oz": weight}

    @property
    def as_kilograms(self) -> dict:
        weight = self._weight / 1000

        return {"kg": weight}

    @property
    def as_tonnes(self) -> dict:
        weight = self._weight / 1000000

        return {"T": weight}

    @property
    def as_stone(self) -> dict:
        weight = self._weight * 0.00015747

        return {"st": weight}


class Pound(Weight):
    symbol = "lb"

    @property
    def as_ounces(self) -> dict:
        weight = self._weight * 16

        return {"oz": weight}

    @property
    def as_grams(self) -> dict:
        weight = self._weight * 453.59237

        return {"g": weight}

    @property
    def as_kilograms(self) -> dict:
        weight = self._weight * 0.45359237

        return {"kg": weight}

    @property
    def as_tonnes(self) -> dict:
        weight = self._weight / 2204.6

        return {"T": weight}

    @property
    def as_stone(self) -> dict:
        weight = self._weight * 0.071429

        return {"st": weight}


class Ounce(Weight):
    symbol = "oz"

    @property
    def as_pounds(self) -> dict:
        weight = self._weight / 16

        return {"lb": weight}

    @property
    def as_grams(self) -> dict:
        weight = self._weight * 28.34952

        return {"g": weight}

    @property
    def as_kilograms(self) -> dict:
        weight = self._weight * 0.02834952

        return {"kg": weight}

    @property
    def as_tonnes(self) -> dict:
        weight = self._weight / 35274

        return {"T": weight}

    @property
    def as_stone(self) -> dict:
        weight = self._weight * 0.0044643

        return {"st": weight}


class Tonne(Weight):
    symbol = "T"

    @property
    def as_pounds(self) -> dict:
        weight = self._weight * 2204.6

        return {"lb": weight}

    @property
    def as_ounces(self) -> dict:
        weight = self._weight * 35274

        return {"oz": weight}

    @property
    def as_grams(self) -> dict:
        weight = self._weight / 0.0000010000

        return {"g": weight}

    @property
    def as_kilograms(self) -> dict:
        weight = self._weight / 0.0010000

        return {"kg": weight}

    @property
    def as_stone(self) -> dict:
        weight = self._weight * 157.47

        return {"st": weight}


class Stone(Weight):
    symbol = "st"

    @property
    def as_pounds(self) -> dict:
        weight = self._weight * 14

        return {"lb": weight}

    @property
    def as_ounces(self) -> dict:
        weight = self._weight * 224

        return {"oz": weight}

    @property
    def as_grams(self) -> dict:
        weight = self._weight / 0.00015747

        return {"g": weight}

    @property
    def as_kilograms(self) -> dict:
        weight = self._weight / 0.15747

        return {"kg": weight}

    @property
    def as_tonnes(self) -> dict:
        weight = self._weight / 157.47

        return {"T": weight}
