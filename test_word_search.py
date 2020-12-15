import unittest
from word_search import *

board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"

class TestSolution(unittest.TestCase):
    def test_exist(self):
        self.assertEqual((self.exist_word(board, word)), True)


if __name__ == "__main__":
    unittest.main()
