
class Instructions_decoder:

    INSTRUCTIONS = ["lw", "sw", "add", "bne", "ori", "nand", "j"]

    def decode(self, instruction):
        instruction = instruction.lower()

        if instruction not in self.INSTRUCTIONS:
            raise ValueError("Instruction not supported")

        return instruction
