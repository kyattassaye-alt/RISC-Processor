
import unittest

from src.sign_zero_extend import ImmediateExtender


class TestImmediateExtender(unittest.TestCase):

    def test_sign_extend_positive(self):
        result = ImmediateExtender.sign_extend(10)
        self.assertEqual(result, 10)

    def test_sign_extend_negative(self):
        result = ImmediateExtender.sign_extend(0xFFFF)
        self.assertEqual(result, -1)

    def test_zero_extend(self):
        result = ImmediateExtender.zero_extend(15)
        self.assertEqual(result, 15)


if __name__ == "__main__":
    unittest.main()
