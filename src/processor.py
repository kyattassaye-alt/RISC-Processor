
from src.alu import ALU
from src.register_file import RegisterFile
from src.memory import DataMemory
from src.program_counter import ProgramCounter
from src.multiplexer import Multiplexer
from src.instruction_decoder import Instructions_decoder


class Processor:

    def __init__(self):
        self.decoder = Instructions_decoder()
        self.alu = ALU()
        self.register_file = RegisterFile()
        self.memory = DataMemory()
        self.pc = ProgramCounter()
        self.mux = Multiplexer()

    def execute(self, instruction):

        operation = self.decoder.decode(instruction["op"])

        if operation == "add":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            result, zero = self.alu.execute(rs, rt, "ADD")
            self.register_file.write(instruction["rd"], result)
            self.pc.increment()

        elif operation == "nand":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            result, zero = self.alu.execute(rs, rt, "NAND")
            self.register_file.write(instruction["rd"], result)
            self.pc.increment()

        elif operation == "ori":
            rs = self.register_file.read(instruction["rs"])
            immediate = instruction["immediate"] & 0xFFFF

            result, zero = self.alu.execute(rs, immediate, "OR")
            self.register_file.write(instruction["rt"], result)
            self.pc.increment()

        elif operation == "lw":
            rs = self.register_file.read(instruction["rs"])
            address = rs + instruction["offset"]

            value = self.memory.read(address)
            self.register_file.write(instruction["rt"], value)
            self.pc.increment()

        elif operation == "sw":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])
            address = rs + instruction["offset"]

            self.memory.write(address, rt)
            self.pc.increment()

        elif operation == "bne":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            if rs != rt:
                branch_address = self.pc.read() + 4 + (instruction["offset"] * 4)
                self.pc.update(branch_address)
            else:
                self.pc.increment()

        # adding the jump instruction assuming that address contains the calculated jum address

        elif operation == "j":
            jump_address = instruction["address"]
            self.pc.update(jump_address)

        else:
            raise ValueError("Unknown instruction: " + operation)
