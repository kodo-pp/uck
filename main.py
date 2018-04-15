#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import args
import files
import translate

if __name__ == '__main__':
    args = args.parse()
    print(repr(args))
    input_buf = files.try_read(args.source_file)
    c_source_buf = translate.uck_to_c(input_buf)
    files.try_write(args.output_file, c_source_buf)
