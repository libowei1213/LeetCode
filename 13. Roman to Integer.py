class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        length = len(s)
        i = 0
        sum = 0

        while i < length:
            if s[i:].startswith("M"):
                sum += 1000
                i += 1
            elif s[i:].startswith("CM"):
                sum += 900
                i += 2
            elif s[i:].startswith("D"):
                sum += 500
                i += 1
            elif s[i:].startswith("CD"):
                sum += 400
                i += 2
            elif s[i:].startswith("C"):
                sum += 100
                i += 1
            elif s[i:].startswith("XC"):
                sum += 90
                i += 2
            elif s[i:].startswith("L"):
                sum += 50
                i += 1
            elif s[i:].startswith("XL"):
                sum += 40
                i += 2
            elif s[i:].startswith("X"):
                sum += 10
                i += 1
            elif s[i:].startswith("IX"):
                sum += 9
                i += 2
            elif s[i:].startswith("V"):
                sum += 5
                i += 1
            elif s[i:].startswith("IV"):
                sum += 4
                i += 2
            elif s[i:].startswith("I"):
                sum += 1
                i += 1
        return sum