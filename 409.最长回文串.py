#
# @lc app=leetcode.cn id=409 lang=python
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (55.32%)
# Likes:    265
# Dislikes: 0
# Total Accepted:    67.7K
# Total Submissions: 122.3K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
# 
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
# 
# 注意:
# 假设字符串的长度不会超过 1010。
# 
# 示例 1: 
# 
# 
# 输入:
# "abccccdd"
# 
# 输出:
# 7
# 
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
# 
# 
#

# @lc code=start
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        from collections import Counter


        char_dict = Counter()
        char_dict.update(s)

        length = 0

        flag = True

        for _,count in char_dict.most_common():
            if count % 2 == 0:
                length += count
            elif flag:
                length += count
                flag = False
            else:
                length += (count-1)
        return length


# @lc code=end

