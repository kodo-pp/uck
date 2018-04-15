# -*- coding: utf-8 -*-

emitter_begin_string = """#include <stdio.h>

#define BF_MEMSIZE 30000

unsigned char bf_memory[BF_MEMSIZE];
size_t bf_pointer = 0;

int main()
{
    for (size_t i = 0; i < BF_MEMSIZE; ++i) {
        bf_memory[i] = (unsigned char) 0;
    }
"""
emitter_end_string = """    return 0;
}
"""

class Emitter:
    def __init__(self):
        self._nested_loops_count = 0

    def emit_begin(self):
        return emitter_begin_string

    def emit_end(self):
        if self._nested_loops_count != 0:
            raise SyntaxError('missing closing "]" in input file')
        return emitter_end_string

    def emit_inc(self):
        return '    ' * self._nested_loops_count + '    ++bf_memory[bf_pointer];\n'

    def emit_dec(self):
        return '    ' * self._nested_loops_count + '    --bf_memory[bf_pointer];\n'

    def emit_ptr_inc(self):
        return '    ' * self._nested_loops_count + '    bf_pointer = (bf_pointer + 1) % BF_MEMSIZE;\n'

    def emit_ptr_dec(self):
        return '    ' * self._nested_loops_count + '    bf_pointer = (bf_pointer + BF_MEMSIZE - 1) % BF_MEMSIZE;\n'

    def emit_loop_begin(self):
        self._nested_loops_count += 1
        return '    ' * self._nested_loops_count + 'while (bf_memory[bf_pointer]) {\n'

    def emit_loop_end(self):
        self._nested_loops_count -= 1
        if self._nested_loops_count < 0:
            raise SyntaxError('too many closing "]"\'s in input file')
        return '    ' * self._nested_loops_count + '    }\n'

    def emit_char_in(self):
        return '    ' * self._nested_loops_count + '    bf_memory[bf_pointer] = (unsigned char) getchar();\n'

    def emit_char_out(self):
        return '    ' * self._nested_loops_count + '    putchar((char) bf_memory[bf_pointer]);\n'
