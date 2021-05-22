"""
    decoder.py

    This serves as a decoder to read instructions from memory
"""

class Decoder():
    def __init__(self):
        pass

    def decode(self, opcode):
        """
            Receive a value in the 0x0000 format, extract the instruction code and return it
        """

        """
            This was a naive implementation;
            
            A better way of doing this is grab the first and last byte of the opcode. The instruction code will be 1
            byte or 2 bytes, the use-case of the second byte depends only on the first byte's value, so it is easy to
            handle those cases. In the cases where the instruction code is only 1 byte, the second byte should be set
            to 0. The result will be a different and unique two bytes number for every opcode supported, allowing to
            access and execute the respective function in a vector or dictionary with O(1) 
        """
        instruction = ""
        while True:
            if opcode & 0xF000 == 0x0000:
                if opcode & 0x00FF == 0x00E0:
                    instruction = "00E0"
                    break
                elif opcode & 0x00FF == 0x00EE:
                    instruction = "00EE"
                    break
            elif opcode & 0xF000 == 0x1000:
                instruction = "1000"
                break
            elif opcode & 0xF000 == 0x2000:
                instruction = "2000"
                break
            elif opcode & 0xF000 == 0x3000:
                instruction = "3000"
                break
            elif opcode & 0xF000 == 0x4000:
                instruction = "4000"
                break
            elif opcode & 0xF000 == 0x5000:
                instruction = "5000"
                break
            elif opcode & 0xF000 == 0x6000:
                instruction = "6000"
                break
            elif opcode & 0xF000 == 0x7000:
                instruction = "7000"
                break
            elif opcode & 0xF000 == 0x8000:
                if opcode & 0x000F == 0x0000:
                    instruction = "8000"
                    break
                elif opcode & 0x000F == 0x0001:
                    instruction = "8001"
                    break
                elif opcode & 0x000F == 0x0002:
                    instruction = "8002"
                    break
                elif opcode & 0x000F == 0x0003:
                    instruction = "8003"
                    break
                elif opcode & 0x000F == 0x0004:
                    instruction = "8004"
                    break
                elif opcode & 0x000F == 0x0005:
                    instruction = "8005"
                    break
                elif opcode & 0x000F == 0x0006:
                    instruction = "8006"
                    break
                elif opcode & 0x000F == 0x0007:
                    instruction = "8007"
                    break
                elif opcode & 0x000F == 0x000E:
                    instruction = "800E"
                    break
            elif opcode & 0xF00F == 0x9000:
                instruction = "9000"
                break
            elif opcode & 0xF000 == 0xA000:
                instruction = "A000"
                break
            elif opcode & 0xF000 == 0xB000:
                instruction = "B000"
                break
            elif opcode & 0xF000 == 0xC000:
                instruction = "C000"
                break
            elif opcode & 0xF000 == 0xD000:
                instruction = "D000"
                break
            elif opcode & 0xF0FF == 0xB09E:
                instruction = "B09E"
                break
            elif opcode & 0xF0FF == 0xE0A1:
                instruction = "E0A1"
                break
            elif opcode & 0xF0FF == 0xF007:
                instruction = "F007"
                break
            elif opcode & 0xF0FF == 0xF00A:
                instruction = "F00A"
                break
            elif opcode & 0xF0FF == 0xF015:
                instruction = "F015"
                break
            elif opcode & 0xF0FF == 0xF018:
                instruction = "F018"
                break
            elif opcode & 0xF0FF == 0xF01E:
                instruction = "F01E"
                break
            elif opcode & 0xF0FF == 0xF029:
                instruction = "F029"
                break
            elif opcode & 0xF0FF == 0xF033:
                instruction = "F033"
                break
            elif opcode & 0xF0FF == 0xF055:
                instruction = "F055"
                break
            elif opcode & 0xF0FF == 0xF065:
                instruction = "F065"
                break
            break

        if instruction == "":
            return "[ERROR] The operation", opcode, "doesn't exist"
        else:
            return instruction



