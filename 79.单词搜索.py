#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
# https://leetcode-cn.com/problems/word-search/description/
#
# algorithms
# Medium (44.17%)
# Likes:    830
# Dislikes: 0
# Total Accepted:    149.3K
# Total Submissions: 336.9K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
# 
# 
# 
# 示例:
# 
# board =
# [
# ⁠ ['A','B','C','E'],
# ⁠ ['S','F','C','S'],
# ⁠ ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false
# 
# 
# 
# 提示：
# 
# 
# board 和 word 中只包含大写和小写英文字母。
# 1 <= board.length <= 200
# 1 <= board[i].length <= 200
# 1 <= word.length <= 10^3
# 
# 
#

# @lc code=start

import copy

class Solution:


    def find(self, visited, board, x, y, word):

        if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):

            if (x,y) in visited:
                return False
            if board[x][y] == word[0]:
                if len(word) == 1:
                    return True

                # 上
                if self.find(visited + [(x,y)], board, x - 1, y, word[1:]):
                    return True
                # 下
                if self.find(visited+ [(x,y)], board, x + 1, y, word[1:]):
                    return True
                # 左
                if self.find(visited+ [(x,y)], board, x, y - 1, word[1:]):
                    return True
                # 右
                if self.find(visited+ [(x,y)], board, x, y + 1, word[1:]):
                    return True

            else:
                return False


        else:
            return False
        
        
            


    def exist(self, board: List[List[str]], word: str) -> bool:

        row = len(board)
        col = len(board[0])

        visited = []
        

        for x in range(row):
            for y in range(col):
                result = self.find(visited, board, x, y, word)
                if result:
                    return True
        
        return False

# @lc code=end

