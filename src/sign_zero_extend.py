class ImmediateExtender:

    @staticmethod
    def sign_extend(value):
        value = value & 0xFFFF # we only keeo the lower 26 bits 
        if value & 0x8000: #if sign bit is one 
            value = value- 0x10000 # fill the upper 16 bits with one 

        return value

    @staticmethod
    def zero_extend(value):
        return value & 0xFFFF # KEEP the upper bits zero
