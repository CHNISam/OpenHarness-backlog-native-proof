import unittest
from product import ANSWER
class Acceptance(unittest.TestCase):
    def test_product(self):
        self.assertEqual(42, ANSWER)
