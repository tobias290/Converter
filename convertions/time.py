from typing import Union


class Time:
    symbol: str

    def __init__(self, microseconds: Union[float, int]):
        self._microseconds: Union[float, int] = self.__convert_to_int_if_possible(microseconds)
        self._milliseconds: Union[float, int] = self.__convert_to_int_if_possible(self._microseconds / 1000)
        self._seconds: Union[float, int] = self.__convert_to_int_if_possible(self._milliseconds / 1000)
        self._minutes: Union[float, int] = self.__convert_to_int_if_possible(self._seconds / 60)
        self._hours: Union[float, int] = self.__convert_to_int_if_possible(self._minutes / 60)
        self._days: Union[float, int] = self.__convert_to_int_if_possible(self._hours / 24)
        self._weeks: Union[float, int] = self.__convert_to_int_if_possible(self._days / 7)
        self._months: Union[float, int] = self.__convert_to_int_if_possible(self._weeks / 4.345)
        self._years: Union[float, int] = self.__convert_to_int_if_possible(self._months / 12)

    @staticmethod
    def __convert_to_int_if_possible(value: Union[float, int]):
        return int(value) if float(value).is_integer() else value

    def all(self) -> dict:
        options = {
            **self.as_microseconds,
            **self.as_milliseconds,
            **self.as_seconds,
            **self.as_minutes,
            **self.as_hours,
            **self.as_days,
            **self.as_weeks,
            **self.as_months,
            **self.as_years,
        }

        # Removes the weight which was given
        return {k: v for k, v in options.items() if k != self.symbol}

    @property
    def as_microseconds(self) -> dict:
        return {"μs": self._microseconds}

    @property
    def as_milliseconds(self) -> dict:
        return {"ms": self._milliseconds}

    @property
    def as_seconds(self) -> dict:
        return {"s": self._seconds}

    @property
    def as_minutes(self) -> dict:
        return {"min": self._minutes}

    @property
    def as_hours(self) -> dict:
        return {"hr": self._hours}

    @property
    def as_days(self) -> dict:
        return {"d": self._days}

    @property
    def as_weeks(self) -> dict:
        return {"wk": self._weeks}

    @property
    def as_months(self):
        return {"m": self._months}

    @property
    def as_years(self):
        return {"yr": self._years}


class Microsecond(Time):
    symbol = "μs"

    def __init__(self, milliseconds: Union[float, int]):
        super().__init__(float(milliseconds))


class Millisecond(Time):
    symbol = "ms"

    def __init__(self, milliseconds: Union[float, int]):
        microseconds = float(milliseconds) * 1000

        super().__init__(microseconds)


class Second(Time):
    symbol = "s"

    def __init__(self, seconds: Union[float, int]):
        microseconds = float(seconds) * 1000 * 1000

        super().__init__(microseconds)


class Minute(Time):
    symbol = "min"

    def __init__(self, minutes: Union[float, int]):
        microseconds = float(minutes) * 6e+7

        super().__init__(microseconds)


class Hour(Time):
    symbol = "hr"

    def __init__(self, hours: Union[float, int]):
        microseconds = float(hours) * 3.6e+9

        super().__init__(microseconds)


class Day(Time):
    symbol = "d"

    def __init__(self, days: Union[float, int]):
        microseconds = float(days) * 8.64e+10

        super().__init__(microseconds)


class Week(Time):
    symbol = "w"

    def __init__(self, weeks: Union[float, int]):
        microseconds = float(weeks) * 6.048e+11

        super().__init__(microseconds)


class Month(Time):
    symbol = "m"

    def __init__(self, months: Union[float, int]):
        microseconds = float(months) * 2.628e+12

        super().__init__(microseconds)


class Year(Time):
    symbol = "yr"

    def __init__(self, years: Union[float, int]):
        microseconds = float(years) * 3.154e+13

        super().__init__(microseconds)
