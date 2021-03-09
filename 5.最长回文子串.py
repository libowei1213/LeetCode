#
# @lc app=leetcode.cn id=5 lang=python
#
# [5] 最长回文子串
#
# https://leetcode-cn.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (33.28%)
# Likes:    3316
# Dislikes: 0
# Total Accepted:    501.6K
# Total Submissions: 1.5M
# Testcase Example:  '"babad"'
#
# 给你一个字符串 s，找到 s 中最长的回文子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
# 
# 
# 示例 2：
# 
# 
# 输入：s = "cbbd"
# 输出："bb"
# 
# 
# 示例 3：
# 
# 
# 输入：s = "a"
# 输出："a"
# 
# 
# 示例 4：
# 
# 
# 输入：s = "ac"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由数字和英文字母（大写和/或小写）组成
# 
# 
#

# @lc code=start


from collections import defaultdict

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        dp = [ [False] * n for _ in range(n) ]

        ans = ""

        for l in range(n):
            for i in range(n):
                j = i + l
                
                if j >= n:
                    break

                if i == j:
                    dp[i][j] = True
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                if dp[i][j]:
                    if j - i + 1 > len(ans):
                        ans = s[i:j+1]
                    
        return ans
                    


# @lc code=end

