"""Здесь надо написать тесты с использованием pytest для модуля item."""
import unittest
from src.item import Item

class testItem(unittest.TestCase):
    def test_calculate_total_price(self):
        item1 = Item('Смартфон', 10000, 20)
        self.assertEqual(item1.calculate_total_price(), 200000)

    def test_apply_discount(self):
        item1 = Item('Смартфон', 10000, 20)
        Item.pay_rate = 0.8
        self.assertEqual(item1.apply_discount(), 8000)

if __name__ == '__main__':
    unittest.main()