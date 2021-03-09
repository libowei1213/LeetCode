#
# @lc app=leetcode.cn id=345 lang=python
#
# [345] 反转字符串中的元音字母
#
# https://leetcode-cn.com/problems/reverse-vowels-of-a-string/description/
#
# algorithms
# Easy (50.84%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    57.9K
# Total Submissions: 113.1K
# Testcase Example:  '"hello"'
#
# 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
# 
# 
# 
# 示例 1：
# 
# 输入："hello"
# 输出："holle"
# 
# 
# 示例 2：
# 
# 输入："leetcode"
# 输出："leotcede"
# 
# 
# 
# 提示：
# 
# 
# 元音字母不包含字母 "y" 。
# 
# 
#

# @lc code=start
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        indices = []
        chars = []

        alphabets = set(['a', 'e', 'i', 'o', 'u','A','E','I','O','U'])

        for i, char in enumerate(s):
            if char in alphabets:
                indices.append(i)
                chars.append(char)

        output = [c for c in s]
        for i, index in enumerate(indices):
            output[index] = chars[-(i + 1)]
        return "".join(output)
        
# @lc code=end

