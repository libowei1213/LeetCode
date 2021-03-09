#
# @lc app=leetcode.cn id=168 lang=python
#
# [168] Excel表列名称
#
# https://leetcode-cn.com/problems/excel-sheet-column-title/description/
#
# algorithms
# Easy (38.45%)
# Likes:    277
# Dislikes: 0
# Total Accepted:    36.7K
# Total Submissions: 95.4K
# Testcase Example:  '1'
#
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
# 
# 例如，
# 
# ⁠   1 -> A
# ⁠   2 -> B
# ⁠   3 -> C
# ⁠   ...
# ⁠   26 -> Z
# ⁠   27 -> AA
# ⁠   28 -> AB 
# ⁠   ...
# 
# 
# 示例 1:
# 
# 输入: 1
# 输出: "A"
# 
# 
# 示例 2:
# 
# 输入: 28
# 输出: "AB"
# 
# 
# 示例 3:
# 
# 输入: 701
# 输出: "ZY"
# 
# 
#

# @lc code=start
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        result = []

        while n > 0:
            result.append((n-1) % 26)
            n = (n-1) // 26
        
        return "".join([chr(ord("A")+i) for i in result[::-1]])

# @lc code=end


if __name__ == '__main__':
    Solution().convertToTitle(701)
    