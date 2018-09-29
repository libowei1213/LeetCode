class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        m = len(matrix[0])

        inf = float("inf")

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    for x in range(n):
                        matrix[x][j] = inf if matrix[x][j] != 0 else 0
                    for x in range(m):
                        matrix[i][x] = inf if matrix[i][x] != 0 else 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == inf:
                    matrix[i][j] = 0

