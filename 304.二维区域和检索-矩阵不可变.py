#
# @lc app=leetcode.cn id=304 lang=python
#
# [304] 二维区域和检索 - 矩阵不可变
#
# https://leetcode-cn.com/problems/range-sum-query-2d-immutable/description/
#
# algorithms
# Medium (47.34%)
# Likes:    221
# Dislikes: 0
# Total Accepted:    43K
# Total Submissions: 81.1K
# Testcase Example:  '["NumMatrix","sumRegion","sumRegion","sumRegion"]\n' +
  '[[[[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]],[2,1,4,3],[1,1,2,2],[1,2,2,4]]'
#
# 给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。
# 
# 
# 上图子矩阵左上角 (row1, col1) = (2, 1) ，右下角(row2, col2) = (4, 3)，该子矩形内元素的总和为 8。
# 
# 
# 
# 示例：
# 
# 
# 给定 matrix = [
# ⁠ [3, 0, 1, 4, 2],
# ⁠ [5, 6, 3, 2, 1],
# ⁠ [1, 2, 0, 1, 5],
# ⁠ [4, 1, 0, 1, 7],
# ⁠ [1, 0, 3, 0, 5]
# ]
# 
# sumRegion(2, 1, 4, 3) -> 8
# sumRegion(1, 1, 2, 2) -> 11
# sumRegion(1, 2, 2, 4) -> 12
# 
# 
# 
# 
# 提示：
# 
# 
# 你可以假设矩阵不可变。
# 会多次调用 sumRegion 方法。
# 你可以假设 row1 ≤ row2 且 col1 ≤ col2 。
# 
# 
#

# @lc code=start

from collections import defaultdict

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """

        sums = defaultdict(int)

        for i in range(len(matrix)):
          for j in range(len(matrix[i])):
            sums[(i, j)] = sums[(i, j - 1)] + matrix[i][j]
            

        self.sums = sums
        self.matrix = matrix




    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """

        total = 0

        for row in range(row1, row2 + 1):
          total += (self.sums[(row, col2)] - self.sums[((row, col1))] + self.matrix[row][col1])
          
        return  total


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
# @lc code=end

