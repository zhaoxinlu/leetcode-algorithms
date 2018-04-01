# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-01
算法思想：Word Search--回溯
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if word == '':
            return True

        row = len(board)
        col = len(board[0])
        visited = [[False] * col for i in range(row)]

        for i in range(row):
            for j in range(col):
                if self.helper(board, word, visited, i, j):
                    return True

        return False

    def helper(self, board, word, visited, row, col):
        if word == '':
            return True

        if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
            return False

        if word[0] == board[row][col] and not visited[row][col]:
            visited[row][col] = True
            if self.helper(board, word[1:], visited, row-1, col) or self.helper(board, word[1:], visited, row+1, col) or self.helper(board, word[1:], visited, row, col-1) or self.helper(board, word[1:], visited, row, col+1):
                return True
            else:
                visited[row][col] = False
        return False

if __name__ == '__main__':
    b = [['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']]
    w = 'SEE'
    print Solution().exist(b, w)