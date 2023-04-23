"""Здесь надо написать тесты с использованием pytest для модуля item."""
import unittest
from src.item import Item
from src.phone import Phone

class testItem(unittest.TestCase):
    # def test_calculate_total_price(self):
    #     item1 = Item('Смартфон', 10000, 20)
    #     self.assertEqual(item1.calculate_total_price(), 200000)
    #
    # def test_apply_discount(self):
    #     item1 = Item('Смартфон', 10000, 20)
    #     Item.pay_rate = 0.8
    #     self.assertEqual(item1.apply_discount(), 8000)
    def setUp(self):
        self.item1 = Item('Смартфон', 10000, 20)
        self.phone1 = Phone("iPhone 14", 120_000, 5, 2)
    def test__repr__(self):
        item1 = Item('Смартфон', 10000, 20)
        self.assertEqual(item1.__repr__(), "Item('Смартфон', 10000, 20)")

    def test__str__(self):
        item1 = Item('Смартфон', 10000, 20)
        self.assertEqual(item1.__str__(), 'Смартфон')

    def test__add__(self):
        self.assertEqual((int(self.item1.quantity) + int(self.phone1.quantity)), 25)




if __name__ == '__main__':
    unittest.main()