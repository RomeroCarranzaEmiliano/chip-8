"""
    chip8.py

"""

class Display():
    def __init__(self):
        """

        """
        pass

    def clear(self):
        """
            Clear the display
        """


class Chip():
    def __init__(self, display, instruction_dictionary):
        """
            Create the chip8 registers as a dictionary, also add timers
            Perhaps also add stack!! -> need more research about this
        """

        # Init registers
        self.registers = {
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

            # Stack
            "S": [0x0]*12
        }

        # Init instructions
        self.execute = instruction_dictionary

        # Init display
        self.display = display

    def as_str(self):
        """
            Return the instance's data as str
        """

        str = "Registers\n"
        str += f"V0: {self.registers['V0']} V1: {self.registers['V1']} " \
               f"V2: {self.registers['V2']} V3: {self.registers['V3']}\n"
        str += f"V4: {self.registers['V4']} V5: {self.registers['V5']} " \
               f"V6: {self.registers['V6']} V7: {self.registers['V7']} \n"
        str += f"V8: {self.registers['V8']} V9: {self.registers['V9']} " \
               f"VA: {self.registers['VA']} VB: {self.registers['VB']}\n"
        str += f"VC: {self.registers['VC']} VD: {self.registers['VD']} " \
               f"VE: {self.registers['VE']} VF: {self.registers['VF']}\n"
        str += f"PC: {self.registers['PC']} SP: {self.registers['SP']} I: {self.registers['I']} \n"
        str += f"DT: {self.registers['DT']} ST: {self.registers['ST']}\n\n"
        str += f"Stack: {self.registers['S']}\n"

        return str

