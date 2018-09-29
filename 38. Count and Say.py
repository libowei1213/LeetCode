class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        else:
            temp = "11"
            for i in range(2, n):
                temp = self.summary(temp)
            return temp

    def summary(self, ss):

        result = ""
        temp = ss[0:1]
        count = 0
        for s in ss:
            if s != temp:
                result += (str(count) + temp)
                temp = s
                count = 1
            else:
                count += 1
        result += (str(count) + temp)
        return result


if __name__ == '__main__':
    r = Solution().countAndSay(3)
    print(r)
