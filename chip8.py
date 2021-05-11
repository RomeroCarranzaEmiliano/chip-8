"""
    chip8.py

"""



class Chip8():
    def __init__(self):
        """
            Create the chip8 registers as a dictionary, also add timers
            Perhaps also add stack!! -> need more research about this
        """
        registers = {
            # VX registers
            "V0": 0x0, "V1": 0x0, "V2": 0x0, "V3": 0x0,
            "V4": 0x0, "V5": 0x0, "V6": 0x0, "V7": 0x0,
            "V8": 0x0, "V9": 0x0, "VA": 0x0, "VB": 0x0,
            "VC": 0x0, "VD": 0x0, "VE": 0x0, "VF": 0x0,

            # Special use registers
            "PC": 0x0,
            "SP": 0x0,
            "I": 0x0,

            # Timers: DT -> delay timer & ST -> sound timer
            "DT": 0x0,
            "ST": 0x0,
        }

