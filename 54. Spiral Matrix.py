class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        n1 = len(matrix)

        if n1 == 0:
            return []

        m1 = len(matrix[0])

        n0 = 0
        m0 = 0

        answers = []

        x, y = 0, 0
        while n1 > n0 or m1 > m0:

            for y in range(m0, m1):
                answers.append(matrix[x][y])
            n0 += 1
            for x in range(n0, n1):
                answers.append(matrix[x][y])
            m1 -= 1
            for y in range(m1 - 1, m0 - 1, -1):
                answers.append(matrix[x][y])
            n1 -= 1
            for x in range(n1 - 1, n0 - 1, -1):
                answers.append(matrix[x][y])
            m0 += 1

        return answers[:len(matrix) * len(matrix[0])]