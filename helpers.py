from typing import Union


def set_to_middle(screen_width: Union[int, float], widget_width: Union[int, float]) -> Union[int, float]:
    """
    Gets the value for a widget to be centred
    :param screen_width: Width of the screen currently
    :param widget_width: Width of the widget
    :return: Returns the X position that would put the widget in the middle of the screen
    """
    return (screen_width / 2) - int(widget_width / 2)


class ListHelper:
    """
    Take a list and records the current, previous and next element in the list
    """
    def __init__(self, arr: list):
        self.__arr: list = arr
        self.__i: int = 0

    @property
    def previous(self):
        """
        Returns the element before the current element.
        If the current element is the first in the list then the previous element will be the last item in the list
        """
        return self.__arr[-1] if self.__i == 0 else self.__arr[self.__i - 1]

    @property
    def current(self):
        """
        Returns the current element
        """
        return self.__arr[self.__i]

    @property
    def next(self):
        """
        Returns the next element after the current.
        If the current element is the last in the list then the next element will be the first item in the list
        """
        return self.__arr[0] if self.__i == len(self.__arr) - 1 else self.__arr[self.__i + 1]

    def change_previous_to_current(self):
        """
        Changes the index/ current element to be the previous element in the list
        """
        self.__i = len(self.__arr) - 1 if self.__i == 0 else self.__i - 1

    def change_next_to_current(self):
        """
        Changes the index/ current element to be the next element in the list
        """
        self.__i = 0 if self.__i == len(self.__arr) - 1 else self.__i + 1
