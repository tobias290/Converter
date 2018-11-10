from typing import List

from .angle import *
from .number import *
from .length import *
from .speed import *
from .temperature import *
from .time import *
from .weight import *


class Unit:
    def __init__(self, symbol: str, cls: object):
        self.__symbol = symbol
        self.__cls = cls

    def __str__(self):
        return self.__symbol

    def __repr__(self):
        return self.__symbol

    @property
    def symbol(self) -> str:
        return self.__symbol

    @property
    def cls(self) -> object:
        return self.__cls


class Conversion:
    def __init__(self, conversion: str, units: List[Unit]):
        self.__conversion = conversion
        self.__units = units

    def __str__(self):
        return self.__conversion

    def __len__(self):
        return len(self.__units)

    def __getitem__(self, i):
        return self.__units[i]

    def __iter__(self):
        for unit in self.__units:
            yield str(unit)

    def get_unit_from_symbol(self, symbol: str) -> Union[Unit, None]:
        for unit in self.__units:
            if unit.symbol == symbol:
                return unit
        return None


def get_list_from_conversion_name(name):
    if name == "Angle":
        return ANGLES
    elif name == "Number":
        return NUMBERS
    elif name == "Speed":
        return SPEEDS
    elif name == "Temperature":
        return TEMPERATURES
    elif name == "Time":
        return TIMES
    elif name == "Weight":
        return WEIGHTS


CONVERSIONS = [
    "Angle",        # DONE
    # "Length",
    "Number",
    "Speed",
    "Temperature",  # DONE
    "Time",
    "Weight",       # DONE
]

ANGLES = Conversion("Angle", [
    Unit(Degree.symbol, Degree),
    Unit(Radian.symbol, Radian),
    Unit(Gradian.symbol, Gradian),
])

NUMBERS = Conversion("Number", [
    Unit(Decimal.symbol, Decimal),
    Unit(Binary.symbol, Binary),
    Unit(Hexadecimal.symbol, Hexadecimal),
    Unit(Octal.symbol, Octal),
])

SPEEDS = Conversion("Speed", [
    Unit(MilesPerHour.symbol, MilesPerHour),
    Unit(KilometresPerHour.symbol, KilometresPerHour),
    Unit(Knot.symbol, Knot),
    Unit(MetersPerSecond.symbol, MetersPerSecond),
])

TEMPERATURES = Conversion("Temperature", [
    Unit(Celsius.symbol, Celsius),
    Unit(Fahrenheit.symbol, Fahrenheit),
    Unit(Kelvin.symbol, Kelvin),
])

TIMES = Conversion("Time", [
    Unit(Microsecond.symbol, Microsecond),
    Unit(Millisecond.symbol, Millisecond),
    Unit(Second.symbol, Second),
    Unit(Minute.symbol, Minute),
    Unit(Hour.symbol, Hour),
    Unit(Day.symbol, Day),
    Unit(Month.symbol, Month),
    Unit(Year.symbol, Year),
])

WEIGHTS = Conversion("Weight", [
    Unit(Kilogram.symbol, Kilogram),
    Unit(Gram.symbol, Gram),
    Unit(Ounce.symbol, Ounce),
    Unit(Pound.symbol, Pound),
    Unit(Tonne.symbol, Tonne),
    Unit(Stone.symbol, Stone),
])
