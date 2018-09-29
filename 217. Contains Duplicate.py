class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        dict = {}

        for num in nums:
            if num not in dict:
                dict[num] = True
            else:
                return True
        return False
