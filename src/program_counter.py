# stores the address of the current instruction and then move to the other instruction address

class ProgramCounter():

    def __init__(self):
        self.pc =0

    def read(self):
        return self.pc

    def update(self, new_address):
        self.pc = new_address & 0xFFFFFFFF

    def increment(self):
        self.pc = (self.pc +4) & 0xFFFFFFFF