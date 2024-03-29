#
# @lc app=leetcode.cn id=434 lang=python
#
# [434] 字符串中的单词数
#
# https://leetcode-cn.com/problems/number-of-segments-in-a-string/description/
#
# algorithms
# Easy (36.85%)
# Likes:    73
# Dislikes: 0
# Total Accepted:    28.3K
# Total Submissions: 76.9K
# Testcase Example:  '"Hello, my name is John"'
#
# 统计字符串中的单词个数，这里的单词指的是连续的不是空格的字符。
# 
# 请注意，你可以假定字符串里不包括任何不可打印的字符。
# 
# 示例:
# 
# 输入: "Hello, my name is John"
# 输出: 5
# 解释: 这里的单词是指连续的不是空格的字符，所以 "Hello," 算作 1 个单词。
# 
# 
#

# @lc code=start
class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        count = 0
        inword = False

        for char in s:
            if not inword and char != " ":
                count += 1
                inword = True
            if inword and char == " ":
                inword = False
        
        return count
            


        

# @lc code=end

