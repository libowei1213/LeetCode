#
# @lc app=leetcode.cn id=650 lang=python
#
# [650] 只有两个键的键盘
#
# https://leetcode-cn.com/problems/2-keys-keyboard/description/
#
# algorithms
# Medium (51.67%)
# Likes:    254
# Dislikes: 0
# Total Accepted:    17.7K
# Total Submissions: 34.1K
# Testcase Example:  '3'
#
# 最初在一个记事本上只有一个字符 'A'。你每次可以对这个记事本进行两种操作：
# 
# 
# Copy All (复制全部) : 你可以复制这个记事本中的所有字符(部分的复制是不允许的)。
# Paste (粘贴) : 你可以粘贴你上一次复制的字符。
# 
# 
# 给定一个数字 n 。你需要使用最少的操作次数，在记事本中打印出恰好 n 个 'A'。输出能够打印出 n 个 'A' 的最少操作次数。
# 
# 示例 1:
# 
# 
# 输入: 3
# 输出: 3
# 解释:
# 最初, 我们只有一个字符 'A'。
# 第 1 步, 我们使用 Copy All 操作。
# 第 2 步, 我们使用 Paste 操作来获得 'AA'。
# 第 3 步, 我们使用 Paste 操作来获得 'AAA'。
# 
# 
# 说明:
# 
# 
# n 的取值范围是 [1, 1000] 。
# 
# 
#

# @lc code=start


f = {
    1: 0,
    2: 2,
    3: 3,
    4: 4,
    5: 5,
    6: 5,
    7: 7,
    8: 6
}

import math

def func1(x):
    if x in f:
        return f[x]
    
    temp = x
    for i in range(2, x//2+2):
        if x % i == 0:
            div = x // i
            temp = min([temp, func1(i) + div])
            f[x] = temp
    f[x] = temp
    return f[x]


class Solution(object):
    def minSteps(self, n):
        """
        :type n: int
        :rtype: int
        """

        return func1(n)
        
# @lc code=end

