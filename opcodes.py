"""
    opcodes.py

    A dictionary of opcodes with the format:
        {"opcode": opcode_function()}

    NOTE:
        This implementation won't work because it doesn't allow te use of parameters in the opcodes,
        a better solution must be found

"""


def _0nnn(chip):
    """
        This instruction is deprecated
    """
    pass


def _00E0(chip):
    """
        Clear the display
    """

    """
        Note: maybe this should be done with a processor's flag
    """
    chip.display.clear()


def _00EE(chip):
    """
         Set the PC to the address at the top of the stack
    """

    # Top of the stack is 0xC given that it only has 12 positions
    chip.registers["PC"] = 0xC
    if chip.registers["SP"] > 0x0:
        chip.registers["SP"] -= 0x1


def _1nnn(chip)

dictionary = {
    "0nnn": _0nnn,
    "00E0": _00E0,
    "00EE": _00EE,
    "1NNN": _1nnn,
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
}
