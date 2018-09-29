from collections import defaultdict


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        if not s and not p or p == "*":
            return True
        if not p or not s:
            return False

        dp = [[False for i in range(len(s) + 1)] for i in range(len(p) + 1)]
        dp[-1][-1] = True

        for i in range(len(p)):
            if p[i] == "*" and dp[i - 1][-1] == True:
                dp[i][-1] = True

        for i in range(len(p)):
            for j in range(len(s)):
                if p[i] == "*":
                    dp[i][j] = dp[i - 1][j - 1] or dp[i - 1][j] or dp[i][j - 1]
                elif s[j] == p[i] or p[i] == "?":
                    dp[i][j] = dp[i - 1][j - 1]
        return dp[len(p) - 1][len(s) - 1]


if __name__ == '__main__':
    r = Solution().isMatch("abbbba", "a**a*?")
    print(r)
