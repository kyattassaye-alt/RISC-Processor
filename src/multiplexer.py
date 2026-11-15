#selcting one input depending on multiple options 

class Multiplexer:

    @staticmethod
    def selection(input0, input1, select_signal):
        if select_signal == 0:
            return input0
        elif select_signal ==1:
            return input1

        else:
            raise ValueError("Selection signal is invalid")