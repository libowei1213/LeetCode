class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)

        for num in nums:
            while num < 0:
                num += n
            nums[num - 1] -= n

        ans = []
        for i in range(n):
            if i > len(nums) - 1 or nums[i] > 0:
                ans.append(i + 1)
        return ans