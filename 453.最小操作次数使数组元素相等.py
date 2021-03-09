#
# @lc app=leetcode.cn id=453 lang=python
#
# [453] 最小操作次数使数组元素相等
#
# https://leetcode-cn.com/problems/minimum-moves-to-equal-array-elements/description/
#
# algorithms
# Easy (54.89%)
# Likes:    182
# Dislikes: 0
# Total Accepted:    19.3K
# Total Submissions: 35.2K
# Testcase Example:  '[1,2,3]'
#
# 给定一个长度为 n 的 非空 整数数组，每次操作将会使 n - 1 个元素增加 1。找出让数组所有元素相等的最小操作次数。
# 
# 
# 
# 示例：
# 
# 
# 输入：
# [1,2,3]
# 输出：
# 3
# 解释：
# 只需要3次操作（注意每次操作会增加两个元素的值）：
# [1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
# 
# 
#

# @lc code=start
class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        min_val = min(nums)

        ans = 0
        for num in nums:
            ans += (num - min_val)
        return ans
        
# @lc code=end

