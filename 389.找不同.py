#
# @lc app=leetcode.cn id=389 lang=python
#
# [389] 找不同
#
# https://leetcode-cn.com/problems/find-the-difference/description/
#
# algorithms
# Easy (63.52%)
# Likes:    158
# Dislikes: 0
# Total Accepted:    37.5K
# Total Submissions: 58.9K
# Testcase Example:  '"abcd"\n"abcde"'
#
# 给定两个字符串 s 和 t，它们只包含小写字母。
# 
# 字符串 t 由字符串 s 随机重排，然后在随机位置添加一个字母。
# 
# 请找出在 t 中被添加的字母。
# 
# 
# 
# 示例 1：
# 
# 输入：s = "abcd", t = "abcde"
# 输出："e"
# 解释：'e' 是那个被添加的字母。
# 
# 
# 示例 2：
# 
# 输入：s = "", t = "y"
# 输出："y"
# 
# 
# 示例 3：
# 
# 输入：s = "a", t = "aa"
# 输出："a"
# 
# 
# 示例 4：
# 
# 输入：s = "ae", t = "aea"
# 输出："a"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 <= s.length <= 1000
# t.length == s.length + 1
# s 和 t 只包含小写字母
# 
# 
#

# @lc code=start
class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        list_a = [0] * 26
        list_b = [0] * 26

        for char in s:
            list_a[ord(char) - ord("a")] += 1
        
        for char in t:
            list_b[ord(char) - ord("a")] += 1

        for i in range(26):
            if list_b[i] - list_a[i] == 1:
                return chr(i+ord("a"))


# @lc code=end

