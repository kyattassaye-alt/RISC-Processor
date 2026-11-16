# i am going to use unittest framework 


import unittest

from src.processor import Processor


class TestProcessorInstructions(unittest.TestCase):

    def setUp(self):
        # Create a fresh processor before every test
        self.processor = Processor()

    def test_add(self):
        self.processor.register_file.write(8, 10)
        self.processor.register_file.write(9, 15)

        instruction = {
            "op": "add",
            "rs": 8,
            "rt": 9,
            "rd": 10
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.register_file.read(10), 25)
        self.assertEqual(self.processor.pc.read(), 4)

    def test_lw(self):
        self.processor.register_file.write(18, 100)
        self.processor.memory.write(400, 75)

        instruction = {
            "op": "lw",
            "rs": 18,
            "rt": 11,
            "offset": 300
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.register_file.read(11), 75)
        self.assertEqual(self.processor.pc.read(), 4)

    def test_sw(self):
        self.processor.register_file.write(23, 1000)
        self.processor.register_file.write(14, 123)

        instruction = {
            "op": "sw",
            "rs": 23,
            "rt": 14,
            "offset": 400
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.memory.read(1400), 123)
        self.assertEqual(self.processor.pc.read(), 4)

    def test_bne_taken(self):
        self.processor.register_file.write(22, 10)
        self.processor.register_file.write(13, 20)

        instruction = {
            "op": "bne",
            "rs": 22,
            "rt": 13,
            "offset": 200
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.pc.read(), 804)

    def test_bne_not_taken(self):
        self.processor.register_file.write(22, 10)
        self.processor.register_file.write(13, 10)

        instruction = {
            "op": "bne",
            "rs": 22,
            "rt": 13,
            "offset": 200
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.pc.read(), 4)

    def test_nand(self):
        self.processor.register_file.write(8, 10)
        self.processor.register_file.write(9, 12)

        instruction = {
            "op": "nand",
            "rs": 8,
            "rt": 9,
            "rd": 10
        }

        self.processor.execute(instruction)

        self.assertEqual(
            self.processor.register_file.read(10),
            4294967287
        )
        self.assertEqual(self.processor.pc.read(), 4)

    def test_ori(self):
        self.processor.register_file.write(8, 240)

        instruction = {
            "op": "ori",
            "rs": 8,
            "rt": 9,
            "immediate": 0x8000
        }

        self.processor.execute(instruction)

        self.assertEqual(self.processor.register_file.read(9), 0x0000080F0)
        self.assertEqual(self.processor.pc.read(), 4)

    def test_jump(self):
        instruction ={
            "op":"j",
            "target": 100
        }

        self.processor.execute(instruction)
        self.assertEqual(self.processor.pc.read(),400)

    def test_lw_negative_offset(self):
        processor = Processor()

        # Set base address to 500
        processor.register_file.write(8, 500)

        # Store a value at address 496
        processor.memory.write(499, 75)

        instruction = {
            "op": "lw",
            "rs": 8,
            "rt": 9,
            "offset": 0xFFFF
        }

        processor.execute(instruction)

        self.assertEqual(processor.register_file.read(9), 75)

    def test_sw_negative_offset(self):
        processor = Processor()

        # Set base address to 500
        processor.register_file.write(8, 500)

        # the value we want to store 
        processor.register_file.write(9, 123)

        instruction = {
            "op": "sw",
            "rs": 8,
            "rt": 9,
            "offset": 0xFFFF
        }

        processor.execute(instruction)

        self.assertEqual(processor.memory.read(499), 123)

if __name__ == "__main__":
    unittest.main()
