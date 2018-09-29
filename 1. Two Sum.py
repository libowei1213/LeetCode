class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, num in enumerate(nums):
            result = target - num
            if result in hashmap:
                return [hashmap[result], index]
            hashmap[num] = index
        return []
