class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        size = len(nums) - 1

        for index, num in enumerate(nums[::-1]):
            if num == val:
                del nums[size - index]

        return len(nums)