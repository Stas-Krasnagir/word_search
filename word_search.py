class Solution:
    def exist_word(self, board, word):
        word_list = list(word)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self._exist_word(board, word_list, i, j):
                    return True
                print(7)
                return False

    def _exist_word(self, board, word_list, i, j):
        if board[i][j] == str(word_list[0]):
            board[i][j] = "_"
            len_word = len(word_list)
            for z, ch in enumerate(word_list):
                if ch != word_list[len_word - 1]:
                    if i > 0 and self._exist_word(board, word_list[z + 1], i - 1, j):  # верхний
                        print(1)
                        return True
                    if i < len(board) - 1 and self._exist_word(board, word_list[z + 1], i + 1, j):  # нижний
                        print(2)
                        return True
                    if j > 0 and self._exist_word(board, word_list[z + 1], i, j - 1):  # левый
                        print(3)
                        return True
                    if j < len(board[0]) - 1 and self._exist_word(board, word_list[z + 1], i, j + 1):  # правый
                        print(4)
                        return True
                print(5)
                return False
        else:
            print(6)
            return False


board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
word = "ABCCED"

test = Solution()
print(test.exist_word(board, word))
