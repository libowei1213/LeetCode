from collections import defaultdict
from sys import maxsize


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dp = defaultdict(lambda: maxsize)
        dp[(0, 0)] = grid[0][0]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i > 0 or j > 0:
                    dp[(i, j)] = min(dp[(i - 1, j)], dp[(i, j - 1)]) + grid[i][j]

        return dp[(len(grid) - 1, len(grid[0]) - 1)]


if __name__ == '__main__':
    r = Solution().minPathSum([
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ])
    print(r)
