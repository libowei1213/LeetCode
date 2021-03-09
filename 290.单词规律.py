#
# @lc app=leetcode.cn id=290 lang=python
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (43.75%)
# Likes:    202
# Dislikes: 0
# Total Accepted:    33.3K
# Total Submissions: 76.2K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
# 
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
# 
# 示例1:
# 
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 
# 示例 2:
# 
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 
# 示例 3:
# 
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 
# 示例 4:
# 
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
# 
#

# @lc code=start

from collections import defaultdict

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """

        pattern_dict = defaultdict(list)

        for i, p in enumerate(pattern):
            pattern_dict[p].append(i)
        
        s_list = s.split()
        
        if len(pattern) != len(s_list):
            return False

        if len(set(s_list)) != len(pattern_dict):
            return False

        for key, value in pattern_dict.items():
            if len(set([s_list[i] for i in value])) != 1:
                return False
        
        return True

# @lc code=end


if __name__ == '__main__':
    a = Solution().wordPattern("abba", "dog cat cat dog")
    print(a)
    
