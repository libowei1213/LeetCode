class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        size = len(matrix)

        new_matrix = []

        for row in range(size):
            rows = []
            for col in range(size):
                rows.append(matrix[size - 1 - col][row])
            new_matrix.append(rows)

        for row in range(size):
            for col in range(size):
                matrix[row][col] = new_matrix[row][col]

        return matrix


if __name__ == '__main__':
    input = [[1,2,3],[4,5,6],[7,8,9]]

    r = Solution().rotate(input)
    print(r)
