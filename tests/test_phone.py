import unittest
from src.phone import Phone
class testItem(unittest.TestCase):

    def test__repr__(self):
        phone1 = Phone('iPhone 14', 120000, 5, 2)
        self.assertEqual(phone1.__repr__(), "Phone('iPhone 14', 120000, 5, 2)")
    def test__str__(self):
        phone1 = Phone("iPhone 14", 120000, 5, 2)
        self.assertEqual(phone1.__str__(), "iPhone 14")

if __name__ == '__main__':
    unittest.main()