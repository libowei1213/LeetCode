from collections import defaultdict


def dfs(x, y, board, word, visited):
    if board[x][y] != word[0]:
        return False
    if len(word) == 1:
        return True

    if x - 1 >= 0 and (x - 1, y) not in visited:
        if dfs(x - 1, y, board, word[1:], visited + [(x - 1, y)]):
            return True
    if x + 1 < len(board) and (x + 1, y) not in visited:
        if dfs(x + 1, y, board, word[1:], visited + [(x + 1, y)]):
            return True
    if y - 1 >= 0 and (x, y - 1) not in visited:
        if dfs(x, y - 1, board, word[1:], visited + [(x, y - 1)]):
            return True
    if y + 1 < len(board[0]) and (x, y + 1) not in visited:
        if dfs(x, y + 1, board, word[1:], visited + [(x, y + 1)]):
            return True

    return False


class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if not board:
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, board, word, [(i, j)]):
                    return True
        return False


if __name__ == '__main__':
    r = Solution().exist(
        [["a", "a"]],
        "aaa")
    print(r)
