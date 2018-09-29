class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x < 0:
            negative = True
            s = str(-x)
        else:
            negative = False
            s = str(x)

        result = int(s[::-1])
        if result > 2 ** 31: return 0
        if negative:
            return -result
        else:
            return result
