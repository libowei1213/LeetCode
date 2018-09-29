class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        matrix = [[0 for i in range(n)] for i in range(n)]

        row = 0
        row1 = n - 1

        col = 0
        col1 = n - 1

        num = 1

        while num <= n * n:

            for i in range(col, col1 + 1):
                if num > n * n:
                    break
                matrix[row][i] = num
                num += 1
            else:
                row += 1

            for i in range(row, row1 + 1):
                if num > n * n:
                    break
                matrix[i][col1] = num
                num += 1
            else:
                col1 -= 1

            for i in range(col1, col - 1, -1):
                if num > n * n:
                    break
                matrix[row1][i] = num
                num += 1
            else:
                row1 -= 1

            for i in range(row1, row - 1, -1):
                if num > n * n:
                    break
                matrix[i][col] = num
                num+=1
            else:
                col += 1

        return matrix


if __name__ == '__main__':

    r = Solution().generateMatrix(3)
    print(r)