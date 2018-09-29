class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        # 检查行
        size = len(board)

        for i in range(size):
            if not self.checkValues(board[i]):
                return False

        # 检查列
        for i in range(size):
            values = [x[i] for x in board]
            if not self.checkValues(values):
                return False

        # 检查 9 个 3*3 格子
        for i in range(3):
            cols = range(i * 3, i * 3 + 3)
            for j in range(3):
                rows = range(j * 3, j * 3 + 3)
                values = [board[r][c] for c in cols for r in rows]
                if not self.checkValues(values):
                    return False

        return True

    def checkValues(self, strs):

        values = [int(s) for s in strs if s != "."]

        occured = {}
        for v in values:
            if v not in occured:
                occured[v] = 0
            else:
                return False
        return True
