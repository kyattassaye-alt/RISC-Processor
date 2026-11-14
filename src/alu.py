class ALU:

    @staticmethod
    def execute(a,b,operation):

        if operation == "ADD":
            result = a + b
        elif operation == "SUB":
            result = a-b

        elif operation == "OR":
            result = a | b 

        elif operation == "NAND":
            result = ~ (a & b)

        else:
            raise ValueError("Invalid ALU operation")

        
        # result staying within 32 bits

        result = result & 0xFFFFFFFF
        zero = (result == 0) #  for the bne instruction

        return result ,zero