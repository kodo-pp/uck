# -*- coding: utf-8 -*-

from sys import stderr

def try_read(filename: str):
    buf = ''
    try:
        with open(filename, 'r') as infile:
            buf = infile.read()
    except Exception as e:
        print('Unable to read from file: ' + str(e), file=stderr)
        exit(1)
    return buf

def try_write(filename: str, data: str):
    try:
        with open(filename, 'w') as outfile:
            outfile.write(data)
    except Exception as e:
        print('Unable to write to file: ' + str(e), file=stderr)
        exit(1)
