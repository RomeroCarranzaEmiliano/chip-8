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
                    instruction = "CLS"
                    break
                elif opcode & 0x00FF == 0x00EE:
                    instruction = "RET"
                    break
            elif opcode & 0xF000 == 0x1000:
                instruction = "JP addr"
                break
            elif opcode & 0xF000 == 0x2000:
                instruction = "CALL addr"
                break
            elif opcode & 0xF000 == 0x3000:
                instruction = "SE Vx, byte"
                break
            elif opcode & 0xF000 == 0x4000:
                instruction = "SNE Vx, byte"
                break
            elif opcode & 0xF000 == 0x5000:
                instruction = "SE Vx, Vy"
                break
            elif opcode & 0xF000 == 0x6000:
                instruction = "LD Vx, byte"
                break
            elif opcode & 0xF000 == 0x7000:
                instruction = "ADD Vx, byte"
                break
            elif opcode & 0xF000 == 0x8000:
                if opcode & 0x000F == 0x0000:
                    instruction = "LD Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0001:
                    instruction = "OR Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0002:
                    instruction = "AND Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0003:
                    instruction = "XOR Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0004:
                    instruction = "ADD Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0005:
                    instruction = "SUB Vx, Vy"
                    break
                elif opcode & 0x000F == 0x0006:
                    instruction = "SHR Vx {, Vy}"
                    break
                elif opcode & 0x000F == 0x0007:
                    instruction = "SUBN Vx, Vy"
                    break
                elif opcode & 0x000F == 0x000E:
                    instruction = "SHL Vx {, Vy}"
                    break
            elif opcode & 0xF00F == 0x9000:
                instruction = "SNE Vx, Vy"
                break
            elif opcode & 0xF000 == 0xA000:
                instruction = "LD I, addr"
                break
            elif opcode & 0xF000 == 0xB000:
                instruction = "JP V0, addr"
                break
            elif opcode & 0xF000 == 0xC000:
                instruction = "RND Vx, byte"
                break
            elif opcode & 0xF000 == 0xD000:
                instruction = "DRW Vx, Vy, nibble"
                break
            elif opcode & 0xF0FF == 0xB09E:
                instruction = "SKP Vx"
                break
            elif opcode & 0xF0FF == 0xE0A1:
                instruction = "SKNP Vx"
                break
            elif opcode & 0xF0FF == 0xF007:
                instruction = "LD Vx, DT"
                break
            elif opcode & 0xF0FF == 0xF00A:
                instruction = "LD Vx, K"
                break
            elif opcode & 0xF0FF == 0xF015:
                instruction = "LD DT, Vx"
                break
            elif opcode & 0xF0FF == 0xF018:
                instruction = "LD ST, Vx"
                break
            elif opcode & 0xF0FF == 0xF01E:
                instruction = "ADD I, Vx"
                break
            elif opcode & 0xF0FF == 0xF029:
                instruction = "LD F, Vx"
                break
            elif opcode & 0xF0FF == 0xF033:
                instruction = "LD B, Vx"
                break
            elif opcode & 0xF0FF == 0xF055:
                instruction = "LD  [I], Vx"
                break
            elif opcode & 0xF0FF == 0xF065:
                instruction = "LD Vx, [I]"
                break
            break

        if instruction == "":
            return "[ERROR] The operation", opcode, "doesn't exist"
        else:
            return instruction



# CODE BELOW IS TESTING ONLY


decoder = Decoder()
print(decoder.decode(0xFE33))

