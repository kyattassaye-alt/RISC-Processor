
from src.alu import ALU
from src.register_file import RegisterFile
from src.memory import DataMemory
from src.program_counter import ProgramCounter
from src.multiplexer import Multiplexer
from src.instruction_decoder import Instructions_decoder
from src.sign_zero_extend import ImmediateExtender


class Processor:

    def __init__(self):
        self.decoder = Instructions_decoder()
        self.alu = ALU()
        self.register_file = RegisterFile()
        self.memory = DataMemory()
        self.pc = ProgramCounter()
        self.mux = Multiplexer()
        self.extender = ImmediateExtender()

    def execute(self, instruction):

        operation = self.decoder.decode(instruction["op"])

        if operation == "add":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            result, zero = self.alu.execute(rs, rt, "ADD")

            #regdst multiplexer for destination
            destination = self.mux.select(
                instruction["rt"],instruction["rd"], 1
            )
            self.register_file.write(destination, result)
            self.pc.increment()

        elif operation == "nand":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            result, zero = self.alu.execute(rs, rt, "NAND")

            #reg dest multiplexer
            destination = self.mux.select(
                instruction["rt"],
                instruction["rd"],
                1
            )
            self.register_file.write(destination, result)
            self.pc.increment()

        elif operation == "ori":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])
            immediate = self.extender.zero_extend(instruction["immediate"])

            # using the mux 
            alu_input_b= self.mux.select(rt,immediate,1) # immediate is input 1

            result, zero = self.alu.execute(rs, alu_input_b, "OR")
            self.register_file.write(instruction["rt"], result)
            self.pc.increment()

        elif operation == "lw":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])
            # adding the sign extend for lw 

            offset = self.extender.sign_extend(instruction["offset"])
            #adding the mux 

            alu_input_b = self.mux.select(rt, offset,1)
            address ,zero= self.alu.execute(rs,alu_input_b, "ADD")

            value = self.memory.read(address)
            self.register_file.write(instruction["rt"], value)
            self.pc.increment()

        elif operation == "sw":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])
            offset = self.extender.sign_extend(instruction["offset"])

            alu_input_b= self.mux.select(rt,offset,1)
            address,zero = self.alu.execute(rs, alu_input_b,"ADD")

            self.memory.write(address, rt)
            self.pc.increment()

        elif operation == "bne":
            rs = self.register_file.read(instruction["rs"])
            rt = self.register_file.read(instruction["rt"])

            #using alu to compare both resistor 

            result, zero = self.alu.execute(rs,rt,"SUB")
            # sign extend to branch offset 

            offset = self.extender.sign_extend(instruction["offset"])
            # both possible nextpc adresses
            pc_plus_4 = self.pc.read()+4
            branch_address= pc_plus_4 +(offset*4)

            #signal with zero
            pc_src= 0 if zero else 1

            nextpc= self.mux.select(pc_plus_4,branch_address,pc_src)
            self.pc.update(nextpc)

        

        # adding the jump instruction assuming that address contains the calculated jum address

        elif operation == "j":
            target = instruction["target"] & 0x03FFFFFF
            jump_address = (
                ((self.pc.read()+4) &0xF0000000) |(target<<2))
            self.pc.update(jump_address)

        else:
            raise ValueError("Unknown instruction: " + operation)
