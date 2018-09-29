class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        l = len(prices)
        if not l:
            return 0

        cur_min = prices[0]
        profit = 0

        for i in range(len(prices)):
            if i > 0:
                cur_min = prices[i] if prices[i] < cur_min else cur_min
            profit = prices[i] - cur_min if prices[i] - cur_min > profit else profit

        return profit


if __name__ == '__main__':
    r = Solution().maxProfit([7, 1, 5, 3, 6, 4])
    print(r)
