# -*- coding: utf-8 -*-
"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

    Integers in each row are sorted from left to right.
    The first integer of each row is greater than the last integer of the previous row.

注意边界值：[], [[1]] and so on.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        rows = len(matrix)

        if rows == 0:
            return False

        cols = len(matrix[0])
        row = 0
        col = cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1

        return False



if __name__ == '__main__':
    print Solution().searchMatrix([], 3)