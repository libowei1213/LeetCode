class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] > nums[i]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)


if __name__ == '__main__':
    r = Solution().lengthOfLIS([1,3,6,7,9,4,10,5,6])
    print(r)
