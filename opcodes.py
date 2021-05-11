"""
    opcodes.py

    A dictionary of opcodes with the format:
        {"opcode": opcode_function()}

"""


def _0NNN():
    """
        Ignored in this interpreter
    """
    pass

def _00NN():



dictionary = {
    "0NNN": _0NNN,
    "00E0": _00EN,
    "OOEE": _00EE,
    "1NNN": _1NNN,
    "2NNN": _2NNN,
    "3XKK": _3XKK,
    "4XKK": _4XKK,
    "5XY0": _5XY0,
    "6XKK": _6XKK,
    "7XKK": _7XKK,
    "8XY0": _8XY0,
    "8XY1": _8XY1,
    "8XY2": _8XY2,
    "8XY3": _8XY3,
    "8XY4": _8XY4,
    "8XY5": _8XY5,
    "8XY6": _8XY6,
    "8XY7": _8XY7,
    "8XYE": _8XYE,
    "9XY0": _9XY0,
    "ANNN": _ANNN,
    "BNNN": _BNNN,
    "CXKK": _CXKK,
    "DXYN": _DXYN,
    "EX9E": _EX9E,
    "EXA1": _EXA1,
    "FX07": _FX07,
    "FX0A": _FX0A,
    "FX15": _FX15,
    "FX18": _FX18,
    "FX1E": _FX1E,
    "FX29": _FX29,
    "FX33": _FX33,
    "FX55": _FX55,
    "FX65": _FX65,
}
