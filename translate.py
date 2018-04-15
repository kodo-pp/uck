# -*- coding: utf-8 -*-
import stream
import emit

def uck_to_c(uck_buf: str):
    uck_stream = stream.CharStream(uck_buf)
    c_stream = stream.CharStream()
    emitter = emit.Emitter()

    c_stream.add(emitter.emit_begin())
    while True:
        ch = uck_stream.next()
        if ch == None:
            break
        elif ch == '+':
            c_stream.add(emitter.emit_inc())
        elif ch == '-':
            c_stream.add(emitter.emit_dec())
        elif ch == '>':
            c_stream.add(emitter.emit_ptr_inc())
        elif ch == '<':
            c_stream.add(emitter.emit_ptr_dec())
        elif ch == '[':
            c_stream.add(emitter.emit_loop_begin())
        elif ch == ']':
            c_stream.add(emitter.emit_loop_end())
        elif ch == '.':
            c_stream.add(emitter.emit_char_out())
        elif ch == ',':
            c_stream.add(emitter.emit_char_in())
        # If nothing suits, we treat this char as a comment
    c_stream.add(emitter.emit_end())
    return c_stream.accumulated_str()
