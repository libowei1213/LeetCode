class Solution:
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if grid == [] or grid == [[]]:
            return 0

        area_xy = 0
        area_xz = 0
        area_yz = [0] * len(grid[0])

        for i in range(len(grid)):
            area_xz += max(grid[i])
            for j in range(len(grid[i])):
                if grid[i][j] != 0:
                    area_xy += 1
                if grid[i][j] > area_yz[j]:
                    area_yz[j] = grid[i][j]

        return area_xy + area_xz + sum(area_yz)
