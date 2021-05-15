"""
    opcodes.py

    A dictionary of opcodes with the format:
        {"opcode": opcode_function()}

    NOTE:
        This implementation(the dictionary implementation) won't work because it doesn't allow te use of parameters in
        the opcodes, a better solution must be found

    - Every instruction is 2 bytes long, so in the format 0x00
    - Among the parameters there are:
        - nnn or 0x0 < 0xC(12): a 12-bit value, the lowest 12 bits of the instruction
        - n or 0x0 < 0x4(4): a 4-bit value, the lowest 4 bits of the instruction
        - x or 0x0 < 0x4(4): a 4-bit value, lower 4 bits of the higher byte of the instruction
        - y or 0x0 < 0x4(4): a 4-bit value, upper 4 bits of the lower byte of the instruction
        - kk or 0x0: an 8-bit value, the lowest 8 bits of the instruction

    - Possible instruction formats
        [COP]   [COP]   [COP]   [COP]
        [COP]   [COP]   [COP]   [ n ]
        [COP]   [COP]   [ k ]   [ k ]
        [COP]   [ n ]   [ n ]   [ n ]
        [COP]   [ x ]   [   ]   [   ]
        [COP]   [ x ]   [ y ]   [   ]
        [COP]   [ x ]   [ k ]   [ k ]
        [COP]   [ x ]   [ y ]   [ n ]
"""




instructions = [
    [], # 0x0
]


#dictionary = {
    #"0nnn": _0nnn, cop=0n000
    #"00E0": _00E0,
    #"00EE": _00EE,
    #"1NNN": _1nnn,
    #"2NNN": _2NNN,
    #"3XKK": _3XKK,
    #"4XKK": _4XKK,
    #"5XY0": _5XY0,
    #"6XKK": _6XKK,
    #"7XKK": _7XKK,
    #"8XY0": _8XY0,
    #"8XY1": _8XY1,
    #"8XY2": _8XY2,
    #"8XY3": _8XY3,
    #"8XY4": _8XY4,
    #"8XY5": _8XY5,
    #"8XY6": _8XY6,
    #"8XY7": _8XY7,
    #"8XYE": _8XYE,
    #"9XY0": _9XY0,
    #"ANNN": _ANNN,
    #"BNNN": _BNNN,
    #"CXKK": _CXKK,
    #"DXYN": _DXYN,
    #"EX9E": _EX9E,
    #"EXA1": _EXA1,
    #"FX07": _FX07,
    #"FX0A": _FX0A,
    #"FX15": _FX15,
    #"FX18": _FX18,
    #"FX1E": _FX1E,
    #"FX29": _FX29,
    #"FX33": _FX33,
    #"FX55": _FX55,
    #"FX65": _FX65,
#}
