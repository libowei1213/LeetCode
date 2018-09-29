import math


class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n <= 0:
            return False

        x = math.log(n, 3)
        if 3**round(x)==n:
            return True
        else:
            return False