class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """

        if x < 0:
            return False

        _str = str(x)

        i = 0
        j = len(_str) - 1

        while i < j:
            if _str[i] != _str[j]:
                return False
            i += 1
            j -= 1
        return True
