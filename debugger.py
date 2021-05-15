"""
    debugger.py

"""

# IMPORT ##########################################################################################
import os


###################################################################################################


def clear():
    if "PYCHARM_HOSTED" in os.environ:
        print("\n" * 100)
    elif os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")


class Debugger():
    def __init__(self, chip, decoder):
        """

        """
        # Init the processor
        self.chip = chip
        self.decoder = decoder
        self.error = ""

    def run(self):
        """

        """

        # Clear the screen once to positionate everything correctly
        clear()
        # Display initial state of the chip
        print(self.chip.as_str())

        # Main loop
        while True:
            # Receive opcode
            opcode = input(">> ")

            # Decode opcode
            """
                There is no need to decode the given opcode, it is already in instruction format
            """

            try:
                self.chip.execute[opcode](self.chip)
                self.error = ""
            except:
                self.error = f"[ERROR] the instruction {opcode} doesn't exist"

            # Clear display
            clear()

            # Display state
            print(self.chip.as_str())

            # Display if error
            if self.error != "":
                print("\n", self.error)

            pass
