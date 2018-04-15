#!/usr/bin/env python3
# -*- coding: utf-8 -*

from sys import stderr

import args
import files
import translate

if __name__ == '__main__':
    args = args.parse()
    input_buf = files.try_read(args.source_file)
    c_source_buf = ''
    try:
        c_source_buf = translate.uck_to_c(input_buf,
                                          default_function=args.default_function,
                                          memory_size=args.memory_size,
                                          do_emit_bf_mem=args.bf_memory)
    except SyntaxError as se:
        print('Uck syntax error: ' + str(se).format(input_file=args.source_file), file=stderr)
    files.try_write(args.output_file, c_source_buf)
