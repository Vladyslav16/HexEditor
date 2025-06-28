'''
helpers
'''
import tkinter as tk

def chunks(data, n):
    return [data[i:i+n] for i in range(0, len(data), n)]

def one_byte_to_ascii(b):
    return chr(b) if 0x1F < b < 0x80 else '.'

def bytes_to_ascii(data):
    return ''.join(one_byte_to_ascii(b) for b in data)

##def edit(editor_instance, bpos, event):
##    byte_num, hex_pos, ascii_pos = bpos
##    hex_index = f'{hex_pos[0]}.{hex_pos[1]}'
##    ascii_index = f'{ascii_pos[0]}.{ascii_pos[1]}'
##
##    if not event.char or not event.char.isprintable():
##        return False
##    if byte_num is None or byte_num >= len(editor_instance.file_data):
##        return False
##
##    # if (курсор на стороні шістнадцяткової частини)
##    if editor_instance.hex_text_widget.index(tk.INSERT) == f"{hex_pos[0]}.{hex_pos[1]}":
##        if event.char in '0123456789abcdefABCDEF':
##            editor_instance.hex_text_widget.delete(hex_index, f'{hex_index}+1c')
##            row, col = hex_pos
##            byte_text = editor_instance.hex_text_widget.get(f'{row}.{col-1}', f'{row}.{col+1}')
##            byte_text = f'{byte_text[0]}{event.char}{byte_text[1]}'.strip().upper()
##            byte_value = int(byte_text, 16)
##            editor_instance.file_data[byte_num] = byte_value
##            editor_instance.hex_text_widget.replace(f'{ascii_pos[0]}.{ascii_pos[1]-1}',
##                                                    f'{ascii_pos[0]}.{ascii_pos[1]}',
##                                                    one_byte_to_ascii(byte_value))
##            return True
##        else:
##            return False
##
##    # if (курсор на стороні хвоста)
##    if editor_instance.hex_text_widget.index(tk.INSERT) == f"{ascii_pos[0]}.{ascii_pos[1]}":
##        if 0x1F < ord(event.char) < 0x80:
##            editor_instance.hex_text_widget.delete(ascii_index, f'{ascii_index}+1c')
##            byte_value = ord(event.char)
##            editor_instance.file_data[byte_num] = byte_value
##            editor_instance.hex_text_widget.replace(f'{hex_pos[0]}.{hex_pos[1]}',
##                                                    f'{hex_pos[0]}.{hex_pos[1]+2}',
##                                                    f'{byte_value:02X}')
##            return True
##        else:
##            return False

##def bInsert(editor_instance, bpos, event):
##    is_valid = edit(editor_instance, bpos, event)
##    try:
##        if is_valid:
##            editor_instance.hex_text_widget.insert(tk.INSERT, event.char.upper())
##            editor_instance.ed_context.highlight_byte(bpos[0], 'insert_highlight')
##    except:
##        print('invalid symbol')

def cursor_position(editor_instance, event=None):
    byte_number = editor_instance.ed_context.cursor_pos_to_byte_number()
    if byte_number is None:
        print('Can not edit here!')
        return "break"
    row, hex_pos, ascii_pos = editor_instance.ed_context.byte_number_to_cursor_pos(byte_number)
    print(f'Byte: {byte_number} | Position: hex({row}, {hex_pos}), ascii({row}, {ascii_pos})')
    editor_instance.ed_context.highlight_byte(byte_number, 'highlight')
