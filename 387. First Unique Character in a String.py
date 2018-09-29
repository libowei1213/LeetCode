from collections import defaultdict


class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        hash = defaultdict(int)

        for char in s:
            hash[char] += 1

        for i, char in enumerate(s):
            if hash[char] == 1:
                return i
        return -1
