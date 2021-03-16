#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (43.02%)
# Likes:    631
# Dislikes: 0
# Total Accepted:    108.8K
# Total Submissions: 251.5K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
# 
# 
# 示例 2：
# 
# 
# 输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
# 
# 
# 
# 
# 提示：
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 
# -100 
# 
# 
#

# @lc code=start
class Solution:

    def print_circle(self,ans, x1, x2, y1, y2, matrix):
        if x1 > x2 or y1 > y2:
            return

        if x1 == x2:
            x = x1
            for y in range(y1, y2 + 1):
                ans.append(matrix[x][y])
            return
        if y1 == y2:
            y = y1
            for x in range(x1, x2 + 1):
                ans.append(matrix[x][y])
            return
        
        x = x1
        y = y1

        for y in range(y1, y2 + 1):
            ans.append(matrix[x][y])
        
        for x in range(x1 + 1, x2 + 1):
            ans.append(matrix[x][y])
            
        for y in range(y2 - 1, y1 - 1, -1):
            ans.append(matrix[x][y])
        
        for x in range(x2 - 1, x1, -1):
            ans.append(matrix[x][y])

        self.print_circle(ans, x1+1,x2-1, y1+1,y2-1, matrix)


    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        ans = []

        x1 = 0
        x2 = len(matrix) - 1

        y1 = 0
        y2 = len(matrix[0])-1 

        self.print_circle(ans, x1, x2, y1, y2, matrix)
        
        return ans


# @lc code=end

