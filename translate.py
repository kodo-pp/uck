# -*- coding: utf-8 -*-
import stream
import emit

def uck_to_c(uck_buf: str, default_function: str, memory_size: int, do_emit_bf_mem: bool):
    uck_stream = stream.CharStream(uck_buf)
    c_stream = stream.CharStream()
    emitter = emit.Emitter(default_function=default_function,
                           memory_size=memory_size,
                           do_emit_bf_mem=do_emit_bf_mem)

    c_stream.add(emitter.emit_begin())
    while True:
        ch = uck_stream.next()
        emitter.debug_newchar()
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
        elif ch == '\n':
            emitter.debug_newline()
        # If nothing suits, we treat this char as a comment
    c_stream.add(emitter.emit_end())
    return c_stream.accumulated_str()
