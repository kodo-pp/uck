# -*- coding: utf-8 -*-

class CharStream:
    def __init__(self, data: str = ''):
        self.data = data
        self._pos = 0

    def add(self, data_to_add: str):
        self.data += data_to_add

    def next(self):
        try:
            ch = self.data[self._pos]
            self._pos += 1
            return ch
        except IndexError:
            return None

    def clear(self):
        self.data = ''
        self._pos = 0

    def reset(self):
        self.seek(0)

    def seek(self, pos: int = 0):
        # TODO: negative positions
        if pos >= len(self.data) or pos < 0:
            raise RangeError('tried to seek to the out-of-range position {}'.format(pos))
        self._pos = pos

    def accumulated_str(self):
        return self.data

    def unread_str(self):
        try:
            return self.data[self._pos:]
        except IndexError:
            return ''
