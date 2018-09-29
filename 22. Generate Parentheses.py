class Solution:

    def count(self, str, char):
        num = 0
        for c in str:
            if c == char:
                num += 1
        return num

    def gen(self, left, right, n):
        if left > right and left < n:
            return ['(', ')']
        elif left == right and left < n:
            return ['(']
        elif left > right and left == n:
            return [')']

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 1:
            return ['()']

        result = ['(']
        for i in range(n * 2 - 1):
            temp = []
            for r in result:
                for c in self.gen(self.count(r, '('), self.count(r, ')'), n):
                    temp.append(r + c)
            result = temp

        return result


if __name__ == '__main__':
    s = Solution()
    r = s.generateParenthesis(3)
    print(r)
