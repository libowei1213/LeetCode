class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:

            n2 = 1
            n1 = 2

            for i in range(3, n + 1):
                temp = n2 + n1
                n2 = n1
                n1 = temp

            return n1
