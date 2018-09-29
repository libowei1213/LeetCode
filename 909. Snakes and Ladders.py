def move(x, n, ladders):
    if x > n * n:
        return None
    if x in ladders:
        return ladders[x]
    else:
        return x


class Solution:
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """

        ladders = {}

        n = len(board)
        numbers = []

        for i in range(n):
            row = [x for x in range(i * n + 1, i * n + n + 1)]
            if i & 1 == 0:
                numbers.insert(0, row)
            else:
                numbers.insert(0, row[::-1])

        for i in range(n):
            for j in range(n):
                if board[i][j] != -1:
                    ladders[numbers[i][j]] = board[i][j]

        start = 1

        queue = [start]

        visited = []

        count = 0
        while queue:
            count += 1
            size = len(queue)
            for _ in range(size):
                x = queue.pop(0)
                for i in range(1, 7):
                    temp = move(x + i, n, ladders)
                    if temp and temp not in visited:
                        if temp == n * n:
                            return count
                        queue.append(temp)
                        visited.append(temp)
        return -1