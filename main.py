from src.alu import ALU
from src.register_file import RegisterFile
from src.memory import DataMemory
from src.instruction_decoder import Instructions_decoder
from src.multiplexer import Multiplexer

result,zero = ALU.execute(5,3,"ADD")
print("ADD:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "SUB")
print("SUB:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "OR")
print("OR:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "NAND")
print("NAND:", result, "Zero:", zero)

# testing read and write register 

rf = RegisterFile()

rf.write(8,25)
rf.write(9,40)
rf.write(10,100)

print("$t0 (Register 8):", rf.read(8))

# testing read and write memory

memory = DataMemory()
memory.write(400,75)
memory.write(500,120)

print("memory[400]:", memory.read(400))

# testing instruction decoder

decoder = Instructions_decoder()

instructions = ["lw","sw","add","bne","nand","ori"]

print("Instruction decoder test")

for instruction in instructions:
    opcode = decoder.decode(instruction)
    print(instruction.upper(), "opcode: ", opcode)


#testing multiplexer

select =Multiplexer()
print("Multiplexer test")
selected_input = select.selection(25,30,0)
print ("Selection 0:", selected_input)
selected_input = select.selection(25,30,1)
print ("Selection 1:", selected_input)
