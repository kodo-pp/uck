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

    def unget(self):
        if self._pos <= 0:
            raise RangeError('unable to unget char: already at the beginning')
        self._pos -= 1

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

    def wait(self, char):
        chars = 0
        lines = 0
        current = ''
        while current != None and current != char:
            current = self.next()
            if current == '\n':
                lines += 1
                chars = 0
            else:
                chars += 1
        return current, chars, lines
