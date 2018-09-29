class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        reverse = digits[::-1]
        result = []

        flag = 1

        for index, num in enumerate(reverse):
            value = num + flag
            if value >= 10:
                value -= 10
                flag = 1
            else:
                flag = 0
            result.append(value)

        if flag:
            result.append(1)

        return result[::-1]