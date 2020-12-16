import unittest
from word_search import *

board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"

class TestSolution(unittest.TestCase):
      def test_exist(self):
          x = Solution()
          res = x.exist_word(board, word)
          self.assertEqual(res, True)


if __name__ == '__main__':
    unittest.main()
