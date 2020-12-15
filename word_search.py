import unittest


class Solution:
    def exist_word(self, board, word):
        word_list = list(word)
        for i in board:
            for j in range(len(board[i])):
                if self._exist_word(board, word_list, i, j):
                    return True
                return False

    def _exist_word(self, board, word_list, i, j):
        if board[i][j] == word_list[0]:
            board[i][j] = "None"
            len_word = len(word_list)
            for z in word_list:
                if i > 0 and z < len_word and self._exist_word(board, word_list[z + 1], i - 1, j):
                    return True
                if i < len(board) - 1 and z < len_word and self._exist_word(board, word_list[z + 1], i + 1, j):
                    return True
                if j > 0 and z < len_word and self._exist_word(board, word_list[z + 1], i, j - 1):
                    return True
                if j < len(board[0]) - 1 and z < len_word and self._exist_word(board, word_list[z + 1], i, j + 1):
                    return True
            return False
        else:
            return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"

class TestSolution(unittest.TestCase):
    def test_exist(self):
        self.assertEqual((self.exist_word(board, word)), True)


if __name__ == "__main__":
    unittest.main()
