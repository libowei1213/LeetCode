#
# @lc app=leetcode.cn id=224 lang=python
#
# [224] 基本计算器
#
# https://leetcode-cn.com/problems/basic-calculator/description/
#
# algorithms
# Hard (39.01%)
# Likes:    367
# Dislikes: 0
# Total Accepted:    28.4K
# Total Submissions: 72.5K
# Testcase Example:  '"1 + 1"'
#
# 实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "1 + 1"
# 输出：2
# 
# 
# 示例 2：
# 
# 
# 输入：s = " 2-1 + 2 "
# 输出：3
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(1+(4+5+2)-3)+(6+8)"
# 输出：23
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
# s 表示一个有效的表达式
# 
# 
#

# @lc code=start
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """



        flag = 1
        stack = [flag]
        i,ans = 0,0

        while i < len(s):
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                flag = stack[-1]
                i+=1
            elif s[i] == '-':
                print("aaaaa")
                flag = stack[-1] * -1
                i+=1
            elif s[i] == '(':
                stack.append(flag)
                i+=1
            elif s[i] == ')':
                stack.pop()
                i+=1
            else:
                j = i
                while j<len(s) and s[j] >= '0' and s[j] <= '9':
                    j+=1
                
                ans += int(s[i:j]) * flag
                print(s[i:j],ans,flag)
                i = j

        return ans
            

# @lc code=end

