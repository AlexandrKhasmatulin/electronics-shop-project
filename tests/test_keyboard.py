import unittest
from src.keyboard import Keyboard

class testItem(unittest.TestCase):
    def test_change_lang(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        self.assertEqual(kb.change_lang().language, 'RU')

