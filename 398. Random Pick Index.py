import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """

        index = 0
        count = 0
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.random() * count < 1:
                    index = i
        return index

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
