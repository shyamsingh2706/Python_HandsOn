# https://leetcode.com/problems/word-search/

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        res = []
        letter_count = 0
        for i in range(rows):
            for j in range(cols):

                if board[i][j] == word[0] and self.dfs(board, i, j, rows, cols, letter_count, word):
                    return True

        return False

    def dfs(self, board, i, j, rows, cols, letter_count , word):

        if letter_count == len(word):
            return True

        if i < 0 or j < 0 or i >= rows or j >= cols or board[i][j] != word[letter_count]:
            return False

        temp = board[i][j]
        board[i][j] = ''

        left = self.dfs(board, i, j - 1, rows, cols, letter_count+1,word)
        right = self.dfs(board, i, j + 1, rows, cols, letter_count+1,word)
        up = self.dfs(board, i - 1, j, rows, cols, letter_count+1,word)
        down = self.dfs(board, i + 1, j, rows, cols, letter_count+1,word)

        board[i][j] = temp

        return left or right or up or down


def main():

    global board

    board = [
            ['A','B','C','E'],
            ['S','F','C','S'],
            ['A','D','E','E']
            ]

    word = "ABCCED"
    sol = Solution()
    print("Word Search is " , sol.exist(board,word))

if __name__ == "__main__":
    main()