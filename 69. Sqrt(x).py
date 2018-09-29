import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        left = 1
        right = math.ceil(x / 2)

        while left <= right:
            mid = (left + right) // 2
            val = mid * mid
            if val == x:
                return mid
            elif val < x:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1
            else:
                if (mid - 1) * (mid - 1) < x:
                    return mid - 1
                right = mid - 1


if __name__ == '__main__':
    r = Solution().mySqrt(1)
    print(r)
