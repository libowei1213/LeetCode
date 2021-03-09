#
# @lc app=leetcode.cn id=383 lang=python
#
# [383] 赎金信
#
# https://leetcode-cn.com/problems/ransom-note/description/
#
# algorithms
# Easy (55.10%)
# Likes:    125
# Dislikes: 0
# Total Accepted:    35.8K
# Total Submissions: 64K
# Testcase Example:  '"a"\n"b"'
#
# 给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串 ransom 能不能由第二个字符串 magazines
# 里面的字符构成。如果可以构成，返回 true ；否则返回 false。
# 
# (题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。杂志字符串中的每个字符只能在赎金信字符串中使用一次。)
# 
# 
# 
# 注意：
# 
# 你可以假设两个字符串均只含有小写字母。
# 
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true
# 
# 
#

# @lc code=start
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        if ransomNote and magazine == "":
            return False

        from collections import Counter

        counter1 = Counter()
        counter2 = Counter()
        counter1.update(ransomNote)
        counter2.update(magazine)

        for word in counter1:
            if word not in counter2:
                return False
            elif counter1[word] > counter2[word]:
                return False
        return True

# @lc code=end

