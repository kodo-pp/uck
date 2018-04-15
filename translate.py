# -*- coding: utf-8 -*-
import stream
import emit

def uck_to_c(uck_buf: str,
             default_function: str,
             memory_size: int,
             do_emit_bf_mem: bool,
             permit_function: bool = True):
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
        elif ch == '*':
            # get function name
            func_name = ''
            while True:
                tmp_ch = uck_stream.next()
                if not tmp_ch.isalnum():
                    uck_stream.unget()
                    break
                emitter.debug_newchar()
                func_name += tmp_ch

            # get opening parenthesis
            dummy, chars, lines = uck_stream.wait('(')
            if dummy == None:
                emitter.syntax_error('expected opening "(" after function name')
            emitter.debug_newline(lines)
            emitter.debug_newchar(chars)

            # get argument type
            argtype, chars, lines = get_type(uck_stream)
            if argtype == None:
                emitter.syntax_error('expected argument type in "()" after function name')
            emitter.debug_newline(lines)
            emitter.debug_newchar(chars)

            # get closing parenthesis
            dummy, chars, lines = uck_stream.wait(')')
            if dummy == None:
                emitter.syntax_error('expected closing ")" after arguments types')
            emitter.debug_newline(lines)
            emitter.debug_newchar(chars)
            rettype, chars, lines = get_type(uck_stream)

            # get return type
            rettype, chars, lines = get_type(uck_stream)
            if rettype == None:
                emitter.syntax_error('expected return type after "()"')
            emitter.debug_newline(lines)
            emitter.debug_newchar(chars)

            # get opening brace
            dummy, chars, lines = uck_stream.wait('{')
            if dummy == None:
                emitter.syntax_error('expected opening "{" after function declaration')
            emitter.debug_newline(lines)
            emitter.debug_newchar(chars)

            # get body and closing brace
            body = ''
            while True:
                body_ch = uck_stream.next()
                if body_ch == None:
                    emitter.syntax_error('expected closing brace after function body')
                elif body_ch == '}':
                    break
                body += body_ch

            # OK, we are done parsing, let's emit!
            emitter.emit_function_beginning(name=func_name, arg_type=argtype, ret_type=rettype)
            uck_to_c(body,
                     default_function=default_function,
                     memory_size=memory_size,
                     do_emit_bf_mem=do_emit_bf_mem,
                     permit_function=False)
            emitter.emit_function_ending()
        elif ch == '\n':
            emitter.debug_newline()
        # If nothing suits, we treat this char as a comment
    c_stream.add(emitter.emit_end())
    return c_stream.accumulated_str()
