#
# @lc app=leetcode.cn id=415 lang=python
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (51.85%)
# Likes:    295
# Dislikes: 0
# Total Accepted:    90.6K
# Total Submissions: 174.7K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 
# 
# 提示：
# 
# 
# num1 和num2 的长度都小于 5100
# num1 和num2 都只包含数字 0-9
# num1 和num2 都不包含任何前导零
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式
# 
# 
#

# @lc code=start
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        num1 = num1[::-1]
        num2 = num2[::-1]

        if len(num1) > len(num2):
            num2 += "0" * (len(num1) - len(num2))
        if len(num2) > len(num1):
            num1 += "0" * (len(num2) - len(num1))


        result = []
        add = 0

        for i, char in enumerate(num1):
            ans = int(num1[i]) + int(num2[i]) + add
            if ans >= 10:
                add = 1
                ans -= 10
            else:
                add = 0
            result.append(str(ans))
        
        if add:
            result.append("1")
        
        print(result)
        return "".join(result[::-1])
        
# @lc code=end

