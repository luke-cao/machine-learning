from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        go through every element of the board, if first letter of word is found, then find next letter againt four
        direction, so for next letters, if word is found, then return true, else return false
        :param board:
        :param word:
        :return:
        """

        def search_word(path: list, word: str) -> bool:
            if len(word) == 0:
                return True

            last_point = path[-1]
            x, y = last_point[0], last_point[1]

            # up cell
            if 0 <= x - 1 < row and (x - 1, y) not in path and board[x - 1][y] == word[0]:
                if search_word(path + [(x - 1, y)], word[1:]):
                    return True

            # dow cell
            if 0 <= x + 1 < row and (x + 1, y) not in path and board[x + 1][y] == word[0]:
                if search_word(path + [(x + 1, y)], word[1:]):
                    return True

            # left cell
            if 0 <= y - 1 < col and (x, y - 1) not in path and board[x][y - 1] == word[0]:
                if search_word(path + [(x, y - 1)], word[1:]):
                    return True

            # right cell
            if 0 <= y + 1 < col and (x, y + 1) not in path and board[x][y + 1] == word[0]:
                if search_word(path + [(x, y + 1)], word[1:]):
                    return True

        row, col = len(board), len(board[0]) if board else 0
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    if search_word([(i, j)], word[1:]):
                        return True
        return False


board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]
word = 'SEE'
print(Solution().exist(board, word))
