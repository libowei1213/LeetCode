class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        reverseA = a[::-1]
        reverseB = b[::-1]

        lenA = len(a)
        lenB = len(b)

        if lenA > lenB:
            size = lenA
        else:
            size = lenB

        result = ''
        flag = 0

        for i in range(size):
            if i < lenA:
                valueA = 1 if reverseA[i] == '1' else 0
            else:
                valueA = 0
            if i < lenB:
                valueB = 1 if reverseB[i] == '1' else 0
            else:
                valueB = 0

            value = valueA + valueB + flag
            if value == 3:
                value = 1
                flag = 1
            elif value == 2:
                value = 0
                flag = 1
            else:
                flag = 0

            result += str(value)

        if flag:
            result += '1'

        return result[::-1]

