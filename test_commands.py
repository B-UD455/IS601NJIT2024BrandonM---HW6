# test_commands.py
import unittest
from commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class TestCalculatorCommands(unittest.TestCase):

    def setUp(self):
        self.add_command = AddCommand()
        self.subtract_command = SubtractCommand()
        self.multiply_command = MultiplyCommand()
        self.divide_command = DivideCommand()

    def test_add(self):
        self.assertEqual(self.add_command.execute(5, 3), 8)
        self.assertEqual(self.add_command.execute(-1, 1), 0)

    def test_subtract(self):
        self.assertEqual(self.subtract_command.execute(10, 4), 6)
        self.assertEqual(self.subtract_command.execute(0, 1), -1)

    def test_multiply(self):
        self.assertEqual(self.multiply_command.execute(3, 7), 21)
        self.assertEqual(self.multiply_command.execute(-1, 5), -5)

    def test_divide(self):
        self.assertEqual(self.divide_command.execute(10, 2), 5)
        with self.assertRaises(ValueError):
            self.divide_command.execute(10, 0)

    
if __name__ == '__main__':
    unittest.main()
