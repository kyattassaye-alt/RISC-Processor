from src.alu import ALU

result,zero = ALU.execute(5,3,"ADD")
print("ADD:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "SUB")
print("SUB:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "OR")
print("OR:", result, "Zero:", zero)

result, zero = ALU.execute(5, 3, "NAND")
print("NAND:", result, "Zero:", zero)