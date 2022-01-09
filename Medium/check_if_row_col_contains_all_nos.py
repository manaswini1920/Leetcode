'''
An n x n matrix is valid if every row and every column contains all the integers from 1 to n (inclusive).

Given an n x n integer matrix matrix, return true if the matrix is valid. Otherwise, return false.
Example 1:
Input: matrix = [[1,2,3],[3,1,2],[2,3,1]]
Output: true
Explanation: In this case, n = 3, and every row and column contains the numbers 1, 2, and 3.
Hence, we return true.

'''


class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        '''
        approach 1: TC :O(n^2) SC:O(n)
        n=len(matrix)
        #checking rows
        for row in matrix:
            if len(set(row))!=n:
                return False
        #invert rows and cols
        new_matrix=[[None]*n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                new_matrix[r][c]=matrix[c][r]

        for row in new_matrix:
            if len(set(row))!=n:
                return False
        return True'''
        #approach 2 TC:O(n^2) SC:O(1)
        n = len(matrix)
        for i in range(n):
            rowxor = colxor = 0
            for j in range(n):
                rowxor ^= matrix[i][j] ^ (j + 1)
                colxor ^= matrix[j][i] ^ (j + 1)
            if rowxor != 0 or colxor != 0:
                return False
        return True





