class Instructions_decoder :

    OPCODES = {
        "lw" : "100011",
        "sw" : "101011",
        "add": "000000",
        "bne": "000100",
        "ori" : "100101",
        "nand": ""
            }

    def decode(self, instruction):
        instruction = instruction.lower()

        if instruction not in self.OPCODES:
            raise ValueError("not in instructions")

        return self.OPCODES[instruction]