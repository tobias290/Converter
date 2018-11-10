from typing import Union


class Number:
    symbol: str

    def __init__(self, number: Union[int, float, str]):
        self._number: Union[int, float, str] = number

    def all(self):
        options = {**self.to_decimal, **self.to_binary, **self.to_hexadecimal, **self.to_octal}

        # Removes the number which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def to_decimal(self):
        return {"dec": self._number}

    @property
    def to_binary(self):
        return {"bin": self._number}

    @property
    def to_hexadecimal(self):
        return {"hex": self._number}

    @property
    def to_octal(self):
        return {"oct": self._number}


class Decimal(Number):
    symbol = "dec"

    @property
    def to_binary(self):
        return {"bin": bin(int(self._number))}

    @property
    def to_hexadecimal(self):
        return {"hex": hex(int(self._number))}

    @property
    def to_octal(self):
        return {"oct": oct(int(self._number))}


class Binary(Number):
    symbol = "bin"

    def __init__(self, number):
        try:
            int(str(number), 2)
        except ValueError:
            number = 0

        super().__init__(number)

    @property
    def to_decimal(self):
        return {"dec": int(str(self._number), 2)}

    @property
    def to_hexadecimal(self):
        return {"hex": hex(int(str(self._number), 2))}

    @property
    def to_octal(self):
        return {"oct": oct(int(str(self._number), 2))}


class Hexadecimal(Number):
    symbol = "hex"

    @property
    def to_decimal(self):
        return {"dec": int(str(self._number), 16)}

    @property
    def to_binary(self):
        return {"bin": bin(int(str(self._number), 16))}

    @property
    def to_octal(self):
        return {"oct": oct(int(str(self._number), 16))}


class Octal(Number):
    symbol = "oct"

    @property
    def to_decimal(self):
        return {"dec": int(str(self._number), 8)}

    @property
    def to_binary(self):
        return {"bin": bin(int(self._number))}

    @property
    def to_hexadecimal(self):
        return {"hex": hex(int(str(self._number), 8))}
