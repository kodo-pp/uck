# -*- coding: utf-8 -*-

import argparse

def parse():
    parser = argparse.ArgumentParser(description='Uck compiler')
    parser.add_argument('source_file',
                        metavar='source',
                        type=str,
                        help='source file')
    parser.add_argument('-o', '--output-file',
                        metavar='output',
                        help='output file (C source)',
                        default='a.out.c')
    parser.add_argument('-f', '--default-function',
                        metavar='func',
                        help='function in which code is located by default (defaults to "main")',
                        default='main')
    parser.add_argument('-m', '--memory-size',
                        metavar='memory_size',
                        help='memory size (in bytes) which may be used by Uck program (defaults to 30000)',
                        type=int,
                        default=30000)
    parser.add_argument('--bf-memory',
                        dest='bf_memory',
                        action='store_const',
                        const=True,
                        default=False,
                        help='put BF memory array to the object file (default: no). Should be used exactly once when building a project')
    return parser.parse_args()
