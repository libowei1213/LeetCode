import math


class Solution:
    def minEatingSpeed(self, piles, H):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """

        if len(piles) == H:
            return max(piles)

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2
            print(mid)
            hours = sum([math.ceil(p / mid) for p in piles])
            if hours > H:
                left = mid + 1
            else:
                right = mid

        return left


if __name__ == '__main__':
    r = Solution().minEatingSpeed([30, 11, 23, 4, 20], 6)
    print(r)

    # print(sum([math.ceil(p / 22) for p in [30, 11, 23, 4, 20]]))
    # print(sum([math.ceil(p / 23) for p in [30, 11, 23, 4, 20]]))