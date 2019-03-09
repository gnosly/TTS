import unittest

from utils.text import phonemes

class SymbolsTest(unittest.TestCase):
    def test_uniqueness(self):
        print("Phoneme" + sorted(phonemes).__str__())
        print("Set    " + sorted(list(set(phonemes))).__str__())
        assert sorted(phonemes) == sorted(list(set(phonemes)))
