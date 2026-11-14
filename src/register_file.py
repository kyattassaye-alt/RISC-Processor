class RegisterFile:

    def __init__(self):
        self.registers =[0]*32 #32 bits registers all starting at zero

    def read(self, register_number):

        if register_number == 0:
            return 0
        
        return self.registers[register_number]
    
    def write(self, register_number, value):

        if register_number == 0:
            return 0
        
        self.registers[register_number]= value & 0xFFFFFFFF
    
    def read_two(self, reg1, reg2):
        return self.read(reg1), self.read(reg2)