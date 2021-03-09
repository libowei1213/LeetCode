#
# @lc app=leetcode.cn id=342 lang=python
#
# [342] 4的幂
#
# https://leetcode-cn.com/problems/power-of-four/description/
#
# algorithms
# Easy (49.24%)
# Likes:    141
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 67.3K
# Testcase Example:  '16'
#
# 给定一个整数 (32 位有符号整数)，请编写一个函数来判断它是否是 4 的幂次方。
# 
# 示例 1:
# 
# 输入: 16
# 输出: true
# 
# 
# 示例 2:
# 
# 输入: 5
# 输出: false
# 
# 进阶：
# 你能不使用循环或者递归来完成本题吗？
# 
#

# @lc code=start
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """

        s = bin(num)[2:]
        if s.startswith("1") and len(s[1:]) % 2 == 0 and not "1" in s[1:]:
            return True
        else:
            return False

        
        
# @lc code=end

