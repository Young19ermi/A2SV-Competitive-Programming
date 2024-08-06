import bisect

class SortedList:
    def __init__(self):
        self._data = []

    def add(self, value):
        index = bisect.bisect_left(self._data, value)
        self._data.insert(index, value)

    def remove(self, value):
        if value in self._data:
            self._data.remove(value)
        else:
            raise ValueError(f"{value}")

    def bisect_left(self, value):
        return bisect.bisect_left(self._data, value)

    def bisect_right(self, value):
        return bisect.bisect_right(self._data, value)

    def __str__(self):
        return str(self._data)

def solve():
     l = SortedList()