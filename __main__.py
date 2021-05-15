"""
    __main__.py

    emulation cycle:
        1) fetch opcode
        2) decode opcode
        3) execute instruction(every opcode must be programmed)
        4) update timers

"""

# IMPORTS #########################################################################################
import debugger as dbg
import chip8
import decoder as dcr
import opcodes
###################################################################################################


def run():
    """
        Ask if want to play or debug mode
    """

    # !!! For now assume debug mode only

    # Initialize the display
    """
        NOTE: maybe put display in a different module
    """
    display = chip8.Display()

    # Import instruction dictionary
    instruction_dictionary = opcodes.dictionary

    # Initialize the processor
    chip = chip8.Chip(display, instruction_dictionary)

    # Initialize the decoder
    decoder = dcr.Decoder()

    debugger = dbg.Debugger(chip, decoder)
    debugger.run()


if __name__ == "__main__":
    run()
