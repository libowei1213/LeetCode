#
# @lc app=leetcode.cn id=91 lang=python3
#
# [91] 解码方法
#

# @lc code=start


class Solution:
    def numDecodings(self, s: str) -> int:

        nums = set([str(i) for i in range(1, 27)])

        from collections import defaultdict

        dp = defaultdict(int)
        if s[0] == "0":
            dp[0] = 0
        else:
            dp[0] = 1

        if s[:2] in nums and len(s[:2]) == 2:
            dp[-1] = 1

        for i in range(1, len(s)):
            if s[i] in nums:
                dp[i] = dp[i-1]
            if s[i - 1:i + 1] in nums:
                dp[i] += dp[i-2]

        return dp[len(s)-1]


# @lc code=end
