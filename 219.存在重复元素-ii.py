#
# @lc app=leetcode.cn id=219 lang=python
#
# [219] 存在重复元素 II
#
# https://leetcode-cn.com/problems/contains-duplicate-ii/description/
#
# algorithms
# Easy (40.47%)
# Likes:    207
# Dislikes: 0
# Total Accepted:    64.2K
# Total Submissions: 158.7K
# Testcase Example:  '[1,2,3,1]\n3'
#
# 给定一个整数数组和一个整数 k，判断数组中是否存在两个不同的索引 i 和 j，使得 nums [i] = nums [j]，并且 i 和 j 的差的
# 绝对值 至多为 k。
# 
# 
# 
# 示例 1:
# 
# 输入: nums = [1,2,3,1], k = 3
# 输出: true
# 
# 示例 2:
# 
# 输入: nums = [1,0,1,1], k = 1
# 输出: true
# 
# 示例 3:
# 
# 输入: nums = [1,2,3,1,2,3], k = 2
# 输出: false
# 
#


# @lc code=start
from collections import defaultdict
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """


        a = defaultdict(list)

        for i,num in enumerate(nums):
            a[num].append(i)
        
        print(a)

        for v in a.values():
            if v:
                if len(v) >= 2:
                    for i in range(len(v) - 1):
                        if v[i+1]-v[i]<=k:
                            return True        
        return False


# @lc code=end

if __name__ == '__main__':
    
    a = Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
    print(a)
    