class Solution:
    def exist_word(self, board, word):

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._exist_word(board, word, i, j):
                    return True
        print(7)
        return False

    def _exist_word(self, board, word, i, j):
        if board[i][j] == word[0]:
            if not word[1:]:
                return True
            board[i][j] = " "
            if i > 0 and self._exist_word(board, word[1:], i - 1, j):  # верхний
                print(1)
                return True
            if i < len(board) - 1 and self._exist_word(board, word[1:], i + 1, j):  # нижний
                print(2)
                return True
            if j > 0 and self._exist_word(board, word[1:], i, j - 1):  # левый
                print(3)
                return True
            if j < len(board[0]) - 1 and self._exist_word(board, word[1:], i, j + 1):  # правый
                print(4)
                return True
            print(5)
            return False
        else:
            print(6)
            return False


