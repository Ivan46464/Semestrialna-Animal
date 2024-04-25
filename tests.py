import unittest
from io import StringIO
from unittest.mock import patch
from Lion import Lion


class AnimalTest(unittest.TestCase):
    def setUp(self):
        self.lion = Lion("Chochko", 4, 220,"Good", "Lion", "Blonde",True, True)

    def test_eat(self):
        food = "Kashuu"
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            self.lion.eat(food)
            printed_value = captured_output.getvalue().strip()

            self.assertEqual(printed_value, "The lion is eating " + food)
    def test_make_sound(self):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.lion.make_sound()
            printed_value = fake_out.getvalue().strip()
            self.assertEqual(printed_value, "Roar")

if __name__ == '__main__':
    unittest.main()
