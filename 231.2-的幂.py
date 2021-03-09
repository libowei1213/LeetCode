#
# @lc app=leetcode.cn id=231 lang=python
#
# [231] 2的幂
#
# https://leetcode-cn.com/problems/power-of-two/description/
#
# algorithms
# Easy (48.67%)
# Likes:    255
# Dislikes: 0
# Total Accepted:    82.9K
# Total Submissions: 170.3K
# Testcase Example:  '1'
#
# 给定一个整数，编写一个函数来判断它是否是 2 的幂次方。
# 
# 示例 1:
# 
# 输入: 1
# 输出: true
# 解释: 2^0 = 1
# 
# 示例 2:
# 
# 输入: 16
# 输出: true
# 解释: 2^4 = 16
# 
# 示例 3:
# 
# 输入: 218
# 输出: false
# 
#

# @lc code=start
from collections import Counter
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        s = bin(n)[2:]
        print(s)
        counter = Counter()
        counter.update(s)
        if s.startswith("1"):
            if counter["1"] == 1:
                return True
        
        return False
# @lc code=end

