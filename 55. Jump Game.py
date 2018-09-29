from collections import defaultdict

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dp = defaultdict(int)

        for i in range(len(nums) - 1, -1, -1):
            dp[i] = i + nums[i]
            for j in range(i, i + nums[i] + 1):
                dp[i] = max(dp[i], dp[j])

        if dp[0] >= len(nums) - 1:
            return True
        else:
            return False