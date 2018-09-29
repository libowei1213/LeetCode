class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash = {}
        for num in nums:
            hash[num] = 1

        longest = 0

        for num in hash.keys():
            if num - 1 not in hash:

                temp = num + 1
                while temp in hash:
                    temp += 1
                longest = max(longest, temp - num)
        return longest