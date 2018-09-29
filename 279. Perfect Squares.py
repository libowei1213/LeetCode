
"""
python3 超时
python2 AC
"""

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """

        # nums = [i ** 2 for i in range(1, int(n ** 0.5) + 1)]
        dp = [float("inf")] * (n + 1)

        for i in range(1, int(n ** 0.5) + 1):
            dp[i ** 2] = 1

        for i in range(2, n + 1):
            for num in range(1, int(n ** 0.5) + 1):
                if num ** 2 <= i:
                    dp[i] = min(dp[i], dp[i - num ** 2] + 1)
                else:
                    break

        return dp[n]


if __name__ == '__main__':
    r = Solution().numSquares(13)
    print(r)
