class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        n = len(obstacleGrid)
        if n == 0:
            return 0

        m = len(obstacleGrid[0])

        dp = [[1] * m] * n

        for i in range(n):
            for j in range(m):

                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    if i > 0 and j > 0:
                        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    elif i > 0:
                        dp[i][j] = dp[i - 1][j]
                    elif j > 0:
                        dp[i][j] = dp[i][j - 1]

        return dp[n - 1][m - 1]