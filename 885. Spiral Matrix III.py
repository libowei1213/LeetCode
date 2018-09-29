class Solution:

    def inArea(self, R, C, r, c):
        if r >= 0 and r < R and c >= 0 and c < C:
            return True
        else:
            return False

    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """

        round = 1
        route = [[r0, c0]]

        r = r0
        c = c0

        while len(route) < R * C:
            # 向右：
            for _ in range(round):
                c += 1
                if self.inArea(R, C, r, c):
                    route.append([r, c])
            # 向下
            for _ in range(round):
                r += 1
                if self.inArea(R, C, r, c):
                    route.append([r, c])
            round += 1
            # 向左
            for _ in range(round):
                c -= 1
                if self.inArea(R, C, r, c):
                    route.append([r, c])

            # 向上
            for _ in range(round):
                r -= 1
                if self.inArea(R, C, r, c):
                    route.append([r, c])

            round += 1

        return route