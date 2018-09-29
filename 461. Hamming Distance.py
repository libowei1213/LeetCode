class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """

        n = (x ^ y)

        count = 0
        while n:
            n = n & (n - 1)
            count += 1

        return count