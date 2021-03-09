#
# @lc app=leetcode.cn id=367 lang=python
#
# [367] 有效的完全平方数
#
# https://leetcode-cn.com/problems/valid-perfect-square/description/
#
# algorithms
# Easy (43.56%)
# Likes:    184
# Dislikes: 0
# Total Accepted:    52.3K
# Total Submissions: 119.9K
# Testcase Example:  '16'
#
# 给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。
# 
# 说明：不要使用任何内置的库函数，如  sqrt。
# 
# 示例 1：
# 
# 输入：16
# 输出：True
# 
# 示例 2：
# 
# 输入：14
# 输出：False
# 
# 
#

# @lc code=start
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """

        left = 0
        right = num // 2 + 1
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

# @lc code=end

