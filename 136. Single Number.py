class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None

        temp = nums[0]

        for num in nums[1:]:
            temp ^= num

        return temp