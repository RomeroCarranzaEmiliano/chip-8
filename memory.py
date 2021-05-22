"""
    memory.py


"""


class Memory():
    def __init__(self):

        # Emulate the memory as an array with 4096 values, each value is 8-bit, so 4096 bytes of memory
        self.memory = [0x0]*4096
        self.fontset = []

    def load_program(self, filename="SpaceInvaders.ch8"):
        """
            Receives the filename of the program, loads it into memory
        """
        file = open("SpaceInvaders.ch8", "rb")
        # The program must start in the 0x200 cell
        self.memory[0x200:] = file.read()
        file.close()



