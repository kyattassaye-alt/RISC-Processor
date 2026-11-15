#Here i am not going to populate every addresss . im only going to store the addresses i need for it 

class DataMemory :

    def __init__(self):
        self.memory = {}

    def read(self, address):

        return self.memory.get(address,0) #return 0 if the address has not been initialized dyet 

    def write (self, address, value):
        self.memory[address] = value & 0xFFFFFFFF