# board.py
class Board:
    def __init__(self, size):
        self._size = size
        self._start = 1
        self._end = self._start + size - 1
