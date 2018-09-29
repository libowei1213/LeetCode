class Solution:
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        N = len(grid)


        hidden = 0
        total = 0

        for i in range(N):
            for j in range(N):
                if j < N - 1:
                    hidden += min(grid[i][j], grid[i][j + 1])
                    hidden += min(grid[j][i], grid[j + 1][i])
                if grid[i][j] > 0:
                    hidden += grid[i][j] - 1

                total += grid[i][j]

        return total * 6 - hidden * 2




if __name__ == '__main__':

    r = Solution().surfaceArea([[2,2,2],[2,1,2],[2,2,2]])
    print(r)