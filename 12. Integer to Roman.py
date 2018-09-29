class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        thousand = num / 1000
        handred = (num - thousand * 1000) / 100
        tens = (num - thousand * 1000 - handred * 100) / 10
        ones = num % 10

        result = ""

        if thousand != 0:
            for i in range(thousand):
                result += "M"

        if handred != 0:
            if handred == 9:
                result += "CM"
            elif handred >= 5:
                result += "D"
                for i in range(handred - 5):
                    result += "C"
            elif handred == 4:
                result += "CD"
            else:
                for i in range(handred):
                    result += "C"

        if tens != 0:
            if tens == 9:
                result += "XC"
            elif tens >= 5:
                result += "L"
                for i in range(tens - 5):
                    result += "X"
            elif tens == 4:
                result += "XL"
            else:
                for i in range(tens):
                    result += "X"

        if ones != 0:
            if ones == 9:
                result += "IX"
            elif ones >= 5:
                result += "V"
                for i in range(ones - 5):
                    result += "I"
            elif ones == 4:
                result += "IV"
            else:
                for i in range(ones):
                    result += "I"

        return result