class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        nowstr = ""
        nowLen = 0
        maxLen = 0

        for c in s:
            if c not in nowstr:
                nowstr += c
                nowLen += 1
            else:
                nowstr = nowstr[nowstr.index(c) + 1:] + c
                if maxLen < nowLen:
                    maxLen = nowLen
                nowLen = len(nowstr)

        if maxLen > nowLen:
            return maxLen
        else:
            return nowLen