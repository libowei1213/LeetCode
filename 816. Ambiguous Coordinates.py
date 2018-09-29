class Solution:

    def judge(self, str):
        if "." in str:
            a, b = str.split(".")
        else:
            a = str
            b = '1'

        if ((len(a) == 1 and a == '0') or not a.startswith('0')) and not b.endswith('0'):
            return True
        else:
            return False

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S.replace("(", "").replace(")", "")
        size = len(S)

        ans = []

        for i in range(1, size):
            num1, num2 = S[:i], S[i:]

            len1 = len(num1)
            len2 = len(num2)

            for l1 in range(0, len1):
                for l2 in range(0, len2):
                    if l1 == 0:
                        left = num1
                    else:
                        left = num1[:l1] + "." + num1[l1:]
                    if l2 == 0:
                        right = num2
                    else:
                        right = num2[:l2] + "." + num2[l2:]

                    if self.judge(left) and self.judge(right):
                        ans.append("(%s, %s)" % (left, right))

        return ans


if __name__ == '__main__':
    r = Solution().ambiguousCoordinates("(100)")
    print(r)
