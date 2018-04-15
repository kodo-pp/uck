# -*- coding: utf-8 -*-

import argparse

def parse():
    parser = argparse.ArgumentParser(description='Uck compiler')
    parser.add_argument('source_file', metavar='source', type=str, help='source file')
    parser.add_argument('-o', '--output-file', metavar='output', help='output file (C source)', default='a.out.c')
    return parser.parse_args()
