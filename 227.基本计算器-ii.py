#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#
# https://leetcode-cn.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (38.94%)
# Likes:    331
# Dislikes: 0
# Total Accepted:    53.7K
# Total Submissions: 126.6K
# Testcase Example:  '"3+2*2"'
#
# 给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
# 
# 整数除法仅保留整数部分。
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "3+2*2"
# 输出：7
# 
# 
# 示例 2：
# 
# 
# 输入：s = " 3/2 "
# 输出：1
# 
# 
# 示例 3：
# 
# 
# 输入：s = " 3+5 / 2 "
# 输出：5
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 由整数和算符 ('+', '-', '*', '/') 组成，中间由一些空格隔开
# s 表示一个 有效表达式
# 表达式中的所有整数都是非负整数，且在范围 [0, 2^31 - 1] 内
# 题目数据保证答案是一个 32-bit 整数
# 
# 
# 
# 
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        sign = 1
        n = len(s)

        i = 0

        while i < n:
            if s[i] == ' ':
                i += 1
            elif s[i] == '+':
                sign = 1
                i += 1
            elif s[i] == '-':
                sign = -1
                i += 1
            elif s[i] == '*' or s[i] == '/':
                j = i + 1
                while j < n and ((s[j] >= '0' and s[j] <= '9') or s[j]==' '):
                    j += 1
                num = int(s[i + 1:j])
                if s[i] == '*':
                    stack[-1] *= num
                elif s[i] == '/':
                    print(stack[-1]/num)
                    stack[-1] = int(stack[-1] / num)
                    
                i = j
            else:
                j = i
                while j < n and s[j] >= '0' and s[j] <= '9':
                    j += 1
                num = int(s[i:j])
                stack.append(sign * num)
                i = j
        
        if stack == []:
            return 0
        return sum(stack)


# @lc code=end

