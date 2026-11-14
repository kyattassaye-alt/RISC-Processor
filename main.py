from src.alu import ALU
from src.register_file import RegisterFile

result,zero = ALU.execute(5,3,"ADD")
print("ADD:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "SUB")
print("SUB:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "OR")
print("OR:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "NAND")
print("NAND:", result, "Zero:", zero)

# testing read and write 

rf = RegisterFile()

rf.write(8,25)
rf.write(9,40)
rf.write(10,100)

print("$t0 (Register 8):", rf.read(8))