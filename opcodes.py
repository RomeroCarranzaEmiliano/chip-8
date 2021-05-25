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

# IMPORTS #########################################################################################
import random
###################################################################################################

def _00E0(chip, _):
    """
        CLS
        Clear the display
    """
    pass

def _00EE(chip, _):
    """
        RET
        Return from a subroutine
        The interpreter sets the program counter to the address at the top of the stack, then substracts 1 from the
        stack pointer
    """
    chip.registers["PC"] = chip.registers["S"][-1]
    chip.registers["SP"] -= 0x1


def _1000(chip, opcode):
    """
        JP addr
        Jump to location nnn
        Sets the program counter to nnn
    """
    # Get the lower 12 bits of the instruction
    addr = opcode & 0x000C

    chip.registers["PC"] = addr


def _2000(chip, opcode):
    """
        CALL addr
        Call subroutine at nnn
        The interpreter increments the stack pointer, then puts the current PC on the top of the stac. The PC then is
        set to nnn
    """
    # Get the lower 12 bits of the instruction
    nnn = opcode & 0x0FFF

    chip.registers["SP"] += 0x1
    chip.registers["S"][-1] = chip.registers["PC"]
    chip.registers["PC"] = nnn


def _3000(chip, opcode):
    """
        SE Vx, byte
        Skip next instruction if Vx = kk.
        The interpreter compares register Vx to kk, and if they are equal, increments the program counter by 2.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    kk = opcode & 0x00FF

    if chip.registers[Vx] == kk:
        chip.registers["PC"] += 0x2


def _4000(chip, opcode):
    """
        SNE Vx, byte
        Skip next instruction if Vx != kk.
        The interpreter compares register Vx to kk, and if they are not equal, increments the program counter by 2.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    kk = opcode & 0x00FF

    if chip.registers[Vx] != kk:
        chip.registers["PC"] += 0x2


def _5000(chip, opcode):
    """
        SE Vx, Vy
        Skip next instruction if Vx = Vy.
        The interpreter compares register Vx to register Vy, and if they are equal, increments the program counter by 2.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    if chip.registers[Vx] == chip.registers[Vy]:
        chip.registers["PC"] += 0x2


def _6000(chip, opcode):
    """
        LD Vx, byte
        Set Vx = kk.
        The interpreter puts the value kk into register Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    kk = opcode & 0x00FF
    chip.registers[Vx] = kk


def _7000(chip, opcode):
    """
        ADD Vx, byte
        Set Vx = Vx + kk.
        Adds the value kk to the value of register Vx, then stores the result in Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    kk = opcode & 0x00FF
    chip.registers[Vx] += kk


def _8000(chip, opcode):
    """
        LD Vx, Vy
        Set Vx = Vy.
        Stores the value of register Vy in register Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    chip.registers[Vx] = chip.registers[Vy]


def _8001(chip, opcode):
    """
        OR Vx, Vy
        Set Vx = Vx OR Vy.
        Performs a bitwise OR on the values of Vx and Vy, then stores the result in Vx.
        A bitwise OR compares the corrseponding bits from two values, and if either bit is 1,
        then the same bit in the result is also 1. Otherwise, it is 0.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    chip.registers[Vx] = chip.registers[Vx] | chip.registers[Vy]


def _8002(chip, opcode):
    """
        AND Vx, Vy
        Set Vx = Vx AND Vy.
        Performs a bitwise AND on the values of Vx and Vy, then stores the result in Vx.
        A bitwise AND compares the corresponding bits from two values, and if both bits are 1,
        then the same bit in the result is also 1. Otherwise, it is 0.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    chip.registers[Vx] = chip.registers[Vx] and chip.registers[Vy]


def _8003(chip, opcode):
    """
        XOR Vx, Vy
        Set Vx = Vx XOR Vy.
        Performs a bitwise exclusive OR on the values of Vx and Vy, then stores the result in Vx.
        An exclusive OR compares the corresponding bits from two values, and if the bits are not both the same,
        then the corresponding bit in the result is set to 1. Otherwise, it is 0.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    chip.registers[Vx] = (chip.registers[Vx] & ~chip.registers[Vy])|(~chip.registers[Vx] & chip.registers[Vy])


def _8004(chip, opcode):
    """
        ADD Vx, Vy
        Set Vx = Vx + Vy, set VF = carry.
        The values of Vx and Vy are added together. If the result is greater than 8 bits (i.e., > 255,) VF is set to 1,
        otherwise 0. Only the lowest 8 bits of the result are kept, and stored in Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    result = chip.registers[Vx] + chip.registers[Vy]
    value = result & 0x000F
    chip.registers[Vx] = value
    chip.registers["VF"] = ((result & 0x00F0) & 0x0010) >> 4


def _8005(chip, opcode):
    """
        SUB Vx, Vy
        Set Vx = Vx - Vy, set VF = NOT borrow.
        If Vx > Vy, then VF is set to 1, otherwise 0. Then Vy is subtracted from Vx, and the results stored in Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    result = chip.registers[Vx] + ~chip.registers[Vy]
    chip.registers[Vx] = result & 0xF
    chip.registers["VF"] = ((result&0x10) >> 4)


def _8006(chip, opcode):
    """
        SHR Vx {, Vy}
        Set Vx = Vx SHR 1.
        If the least-significant bit of Vx is 1, then VF is set to 1, otherwise 0. Then Vx is divided by 2.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    chip.registers["VF"] = chip.registers[Vx] & 0x1
    chip.registers[Vx] //= 2


def _8007(chip, opcode):
    """
        SUBN Vx, Vy
        Set Vx = Vy - Vx, set VF = NOT borrow.
        If Vy > Vx, then VF is set to 1, otherwise 0. Then Vx is subtracted from Vy, and the results stored in Vx.
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    result = chip.registers[Vy] + ~chip.registers[Vx]
    chip.registers[Vx] = result & 0xF
    chip.registers["VF"] = ((result&0x10) >> 4)


def _800E(chip, opcode):
    """
        SHL Vx {, Vy}
        Set Vx = Vx SHL 1.
        If the most-significant bit of Vx is 1, then VF is set to 1, otherwise to 0. Then Vx is multiplied by 2.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    chip.registers["VF"] = chip.registers[Vx] & 0x1
    chip.registers[Vx] *= 0x2


def _9000(chip, opcode):
    """
        SNE Vx, Vy
        Skip next instruction if Vx != Vy.
        The values of Vx and Vy are compared, and if they are not equal,
        the program counter is increased by 2
    """
    x = (opcode & 0x0F00) >> 0x8
    y = (opcode & 0x00F0) >> 0x4
    Vx = f"V{str(x)}"
    Vy = f"V{str(y)}"
    if chip.registers[Vx] != chip.registers[Vy]:
        chip.registers["PC"] += 2


def _A000(chip, opcode):
    """
        LD I, addr
        Set I = nnn.
        The value of register I is set to nnn
    """
    nnn = (opcode & 0x0FFF) >> 4
    chip.registers["I"] = nnn


def _B000(chip, opcode):
    """
        JP V0, addr
        Jump to location nnn + V0.
        The program counter is set to nnn plus the value of V0.
    """
    nnn = (opcode & 0x0FFF) >> 4
    chip.registers["PC"] = nnn + chip.registers["V0"]


def _C000(chip, opcode):
    """
        RND Vx, byte
        Set Vx = random byte AND kk.
        The interpreter generates a random number from 0 to 255, which is then ANDed with the value kk.
        The results are stored in Vx. See instruction 8xy2 for more information on AND.
    """
    x = (opcode & 0x0F00) >> 0x8
    Vx = f"V{str(x)}"
    kk = opcode & 0x00FF
    rnd = random.randint(0, 255)
    chip.registers[Vx] = rnd & kk


def _D000(chip, opcode):
    """
        DRW Vx, Vy, nibble
        Display n-byte sprite starting at memory location I at (Vx, Vy), set VF = collision.
        The interpreter reads n bytes from memory, starting at the address stored in I.
        These bytes are then displayed as sprites on screen at coordinates (Vx, Vy). Sprites are XORed onto the
        existing screen. If this causes any pixels to be erased, VF is set to 1, otherwise it is set to 0.
        If the sprite is positioned so part of it is outside the coordinates of the display,
        it wraps around to the opposite side of the screen. See instruction 8xy3 for more information on XOR,
        and section 2.4, Display, for more information on the Chip-8 screen and sprites.
    """
    


dictionary = {
    "00E0": _00E0,
    "00EE": _00EE,
    "1000": _1000,
    "2000": _2000,
    "3000": _3000,
    "4000": _4000,
    "5000": _5000,
    "6000": _6000,
    "7000": _7000,
    "8000": _8000,
    "8001": _8001,
    "8002": _8002,
    "8003": _8003,
    "8004": _8004,
    "8005": _8005,
    "8006": _8006,
    "8007": _8007,
    "800E": _800E,
    "9000": _9000,
    "A000": _A000,
    "B000": _B000,
    "C000": _C000,
    "D000": _D000,
}


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
