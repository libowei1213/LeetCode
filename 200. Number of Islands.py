def dfs(start, max_x, max_y, visited, grid):
    stack = [start]
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        if 0 <= x + 1 <= max_x and 0 <= y <= max_y and grid[x + 1][y] == "1" and (x + 1, y) not in visited:
            stack.append((x + 1, y))
        if 0 <= x - 1 <= max_x and 0 <= y <= max_y and grid[x - 1][y] == "1" and (x - 1, y) not in visited:
            stack.append((x - 1, y))
        if 0 <= x <= max_x and 0 <= y + 1 <= max_y and grid[x][y + 1] == "1" and (x, y + 1) not in visited:
            stack.append((x, y + 1))
        if 0 <= x <= max_x and 0 <= y - 1 <= max_y and grid[x][y - 1] == "1" and (x, y - 1) not in visited:
            stack.append((x, y - 1))


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0

        max_x = len(grid) - 1
        max_y = len(grid[0]) - 1

        visited = set()

        count = 0
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                if grid[i][j] == "1" and (i, j) not in visited:
                    dfs((i, j), max_x, max_y, visited, grid)
                    count += 1

        return count


if __name__ == '__main__':
    r = Solution().numIslands(
        [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]])
    print(r)
