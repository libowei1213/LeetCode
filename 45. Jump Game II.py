from collections import defaultdict



class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) <= 1:
            return 0

        # dp[i] 表示从第i位置跳到最后的最小步数
        dp = defaultdict(lambda: float("inf"))

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= len(nums) - 1:
                dp[i] = 1

            else:
                for j in range(i, i + nums[i] + 1):
                    dp[i] = min(dp[i], 1 + dp[j])

        return dp[0]
