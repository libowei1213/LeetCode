class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        newstr = "0"

        str = str.strip()

        negative = False

        if str.startswith("+"):
            negative = False
            str = str[1:]
        elif str.startswith("-"):
            negative = True
            str = str[1:]

        for c in str:
            if c >= '0' and c <= '9':
                newstr += c
            else:
                break

        result = int(newstr)

        if negative:
            result = -result

        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result
