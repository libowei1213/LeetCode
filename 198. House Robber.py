class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dp = [nums[0]] * len(nums)

        for i in range(len(nums)):
            if i > 0:
                dp[i] = max(dp[i - 1], nums[i])

            if i >= 2:
                dp[i] = max(dp[i - 1], max(dp[:i - 1]) + nums[i])

        return dp[-1]



if __name__ == '__main__':
    r = Solution().rob([2,1,1,2])
    print(r)