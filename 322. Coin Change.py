class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """

        if not amount:
            return 0

        coins.sort()

        dp = [float("inf")] * (amount + 1)
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1

        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]


if __name__ == '__main__':
    coins = [2]
    amount = 3
    r = Solution().coinChange(coins, amount)
    print(r)
