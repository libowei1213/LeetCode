#
# @lc app=leetcode.cn id=20 lang=python
#
# [20] 有效的括号
#
# https://leetcode-cn.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (43.79%)
# Likes:    2220
# Dislikes: 0
# Total Accepted:    551.9K
# Total Submissions: 1.3M
# Testcase Example:  '"()"'
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
# 
# 有效字符串需满足：
# 
# 
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "()"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "()[]{}"
# 输出：true
# 
# 
# 示例 3：
# 
# 
# 输入：s = "(]"
# 输出：false
# 
# 
# 示例 4：
# 
# 
# 输入：s = "([)]"
# 输出：false
# 
# 
# 示例 5：
# 
# 
# 输入：s = "{[]}"
# 输出：true
# 
# 
# 
# 提示：
# 
# 
# 1 
# s 仅由括号 '()[]{}' 组成
# 
# 
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """


        stack = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            else:
                if stack == []:
                    return False
                else:
                    top = stack.pop()
                    if c == ')' and top != '(':
                        return False
                    if c == ']' and top != '[':
                        return False
                    if c == '}' and top != '{':
                        return False

        if stack:
            return False
            
        return True
            


# @lc code=end

