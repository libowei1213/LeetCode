#
# @lc app=leetcode.cn id=258 lang=python
#
# [258] 各位相加
#
# https://leetcode-cn.com/problems/add-digits/description/
#
# algorithms
# Easy (67.99%)
# Likes:    292
# Dislikes: 0
# Total Accepted:    52.3K
# Total Submissions: 77K
# Testcase Example:  '38'
#
# 给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。
# 
# 示例:
# 
# 输入: 38
# 输出: 2 
# 解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
# 
# 
# 进阶:
# 你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
# 
#

# @lc code=start
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """

        if num <= 9:
            return num
        else:
            return num % 9 if num % 9!=0 else 9

# @lc code=end

