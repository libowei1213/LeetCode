class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        dp = [[1] * m] * n

        for i in range(n):
            for j in range(m):
                if i > 0 and j > 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[n - 1][m - 1]


if __name__ == '__main__':
    r = Solution().uniquePaths(3, 7)
    print(r)
