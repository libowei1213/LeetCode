#
# @lc app=leetcode.cn id=441 lang=python
#
# [441] 排列硬币
#
# https://leetcode-cn.com/problems/arranging-coins/description/
#
# algorithms
# Easy (41.86%)
# Likes:    88
# Dislikes: 0
# Total Accepted:    34.8K
# Total Submissions: 83K
# Testcase Example:  '5'
#
# 你总共有 n 枚硬币，你需要将它们摆成一个阶梯形状，第 k 行就必须正好有 k 枚硬币。
# 
# 给定一个数字 n，找出可形成完整阶梯行的总行数。
# 
# n 是一个非负整数，并且在32位有符号整型的范围内。
# 
# 示例 1:
# 
# 
# n = 5
# 
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤
# 
# 因为第三行不完整，所以返回2.
# 
# 
# 示例 2:
# 
# 
# n = 8
# 
# 硬币可排列成以下几行:
# ¤
# ¤ ¤
# ¤ ¤ ¤
# ¤ ¤
# 
# 因为第四行不完整，所以返回3.
# 
# 
#

# @lc code=start
class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        import math

        x = (-1 + math.sqrt(1 + n * 8)) / 2
        x = math.floor(x)
        return int(x)
        
# @lc code=end

