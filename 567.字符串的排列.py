#
# @lc app=leetcode.cn id=567 lang=python
#
# [567] 字符串的排列
#
# https://leetcode-cn.com/problems/permutation-in-string/description/
#
# algorithms
# Medium (38.26%)
# Likes:    303
# Dislikes: 0
# Total Accepted:    73.4K
# Total Submissions: 176.3K
# Testcase Example:  '"ab"\n"eidbaooo"'
#
# 给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。
# 
# 换句话说，第一个字符串的排列之一是第二个字符串的子串。
# 
# 
# 
# 示例 1：
# 
# 
# 输入: s1 = "ab" s2 = "eidbaooo"
# 输出: True
# 解释: s2 包含 s1 的排列之一 ("ba").
# 
# 
# 示例 2：
# 
# 
# 输入: s1= "ab" s2 = "eidboaoo"
# 输出: False
# 
# 
# 
# 
# 提示：
# 
# 
# 输入的字符串只包含小写字母
# 两个字符串的长度都在 [1, 10,000] 之间
# 
# 
#

# @lc code=start

from collections import Counter


class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        counter1 = Counter()

        counter1.update(s1)

        if len(s1) > len(s2):
            return False

        length = len(s1)

        counter2 = Counter()
        counter2.update(s2[:length])

        for i in range(0, len(s2) - length +1):
            if i == 0:
                counter2 = Counter()
                counter2.update(s2[i:i + length])
            else:
                counter2[s2[i - 1]] -= 1
                if counter2[s2[i - 1]] == 0:
                    del counter2[s2[i - 1]]
                counter2.update(s2[i + length - 1 ])
            if counter1 == counter2:
                return True
            
        if counter1 == counter2:
            return True

        print(counter1)
        print(counter2)

        return False

            


# @lc code=end

