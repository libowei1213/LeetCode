#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] 最长公共子序列
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        from collections import defaultdict
        dp = defaultdict(int)

        max_val = 0

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[(i,j)] = dp[(i-1,j-1)] + 1
                else:
                    dp[(i,j)] = max([dp[(i-1,j)],dp[(i,j-1)]])
                max_val = max([max_val,dp[(i,j)]])
        
        return max_val



# @lc code=end

