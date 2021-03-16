#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#
# https://leetcode-cn.com/problems/merge-intervals/description/
#
# algorithms
# Medium (44.53%)
# Likes:    833
# Dislikes: 0
# Total Accepted:    201.3K
# Total Submissions: 450.7K
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi]
# 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
# 
# 
# 示例 2：
# 
# 
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
# 
# 
# 
# 提示：
# 
# 
# 1 
# intervals[i].length == 2
# 0 i i 
# 
# 
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        intervals.sort(key=lambda x: x[0])
        
        merged_intervals = []
        
        for i, (x, y) in enumerate(intervals):
            if i == 0:
                merged_intervals.append([x, y])
            else:

                # 在上一个区间里
                if merged_intervals[-1][0] <= x < y <= merged_intervals[-1][1]:
                    pass
                # 一半在上一个区间里
                elif merged_intervals[-1][0] <= x <= merged_intervals[-1][1] <= y:
                    merged_intervals[-1][1] = y
                # 不在上一个区间里
                elif merged_intervals[-1][1] < x:
                    merged_intervals.append([x,y])

        return merged_intervals
                    
            

# @lc code=end

