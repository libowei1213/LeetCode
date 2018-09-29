class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        i = 0
        for num in nums:
            if num != 0:
                nums[i] = num
                i += 1

        for k in range(i, len(nums)):
            nums[k] = 0

        print(nums)