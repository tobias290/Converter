from typing import Union


class Length:
    symbol: str

    def __init__(self, length: Union[int, float]):
        self._length = float(length)

    @property
    def length(self) -> float:
        return self._length

    @length.setter
    def length(self, length: Union[int, float]):
        self._length = length

    def all(self) -> dict:
        options = {
            **self.as_nanometre,
            **self.as_micrometre,
            **self.as_centimetre,
            **self.as_metre,
            **self.as_kilometre,
            **self.as_inch,
            **self.as_foot,
            **self.as_yard,
            **self.as_mile,
            **self.as_nautical_mile,
        }

        # Removes the angle which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def as_nanometre(self) -> dict:
        return {"np": self._length}

    @property
    def as_micrometre(self) -> dict:
        return {"μm": self._length}

    @property
    def as_centimetre(self) -> dict:
        return {"cm": self._length}

    @property
    def as_metre(self) -> dict:
        return {"m": self._length}

    @property
    def as_kilometre(self) -> dict:
        return {"km": self._length}

    @property
    def as_inch(self) -> dict:
        return {"in": self._length}

    @property
    def as_foot(self) -> dict:
        return {"ft": self._length}

    @property
    def as_yard(self) -> dict:
        return {"yd": self._length}

    @property
    def as_mile(self) -> dict:
        return {"mi": self._length}

    @property
    def as_nautical_mile(self) -> dict:
        return {"nm": self._length}


class Nanometre(Length):
    symbol = "nm"


class Micrometre(Length):
    symbol = "μm"


class Centimetre(Length):
    symbol = "cm"


class Metre(Length):
    symbol = "m"


class KiloMetre(Length):
    symbol = "km"


class Inch(Length):
    symbol = "in"


class Foot(Length):
    symbol = "ft"


class Yard(Length):
    symbol = "yd"


class Mile(Length):
    symbol = "mi"


class NauticalMile(Length):
    symbol = "nm"
