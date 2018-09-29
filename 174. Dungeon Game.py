from collections import defaultdict


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """

        dp = defaultdict(lambda: float("inf"))

        n = len(dungeon)
        m = len(dungeon[0])

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):

                if i == n - 1 and j == m - 1:
                    dp[(i, j)] = max(1 - dungeon[i][j], 1)
                else:
                    dp[(i, j)] = min(dp[(i, j + 1)], dp[(i + 1, j)]) - dungeon[i][j]
                    dp[(i, j)] = max(dp[(i, j)], 1)

        return dp[(0, 0)]
