class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """

        total = 0
        for i, char in enumerate(s[::-1]):
            total += (ord(char) - ord("A") + 1) * 26 ** i
        return total
