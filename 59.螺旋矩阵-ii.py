#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#
# https://leetcode-cn.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (78.47%)
# Likes:    321
# Dislikes: 0
# Total Accepted:    65.5K
# Total Submissions: 83.5K
# Testcase Example:  '3'
#
# 给你一个正整数 n ，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
# 
# 
# 示例 2：
# 
# 
# 输入：n = 1
# 输出：[[1]]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 
# 
# 
#

# @lc code=start
class Solution:


    def generateMatrix(self, n: int) -> List[List[int]]:



        r0 = 0
        r1 = n - 1
        
        c0 = 0
        c1 = n - 1
        
        matrix = [[0]*n for _ in range(n) ] 

        i = 1
        x,y = 0,0
        while i <= n * n:
            for y in range(c0, c1 + 1):
                if i > n * n:
                    break
                matrix[x][y] = i
                i += 1
                
            r0 += 1
            
            for x in range(r0, r1 + 1):
                if i > n * n:
                    break
                matrix[x][y] = i
                i += 1
                
            c1 -= 1
            
            for y in range(c1, c0 - 1, -1):
                if i > n * n:
                    break
                matrix[x][y] = i
                i += 1
                
            
            r1 -= 1
            
            for x in range(r1, r0 - 1, -1):
                if i > n * n:
                    break
                matrix[x][y] = i
                i += 1
            
            c0 += 1
        
        return matrix
            
                



# @lc code=end

