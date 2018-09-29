import re


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if s == "":
            return True

        left, right = 0, len(s) - 1

        reg = re.compile('[a-zA-Z0-9]')

        while left < right:
            a, b = s[left], s[right]
            if not reg.match(a):
                left += 1
                continue
            if not reg.match(b):
                right -= 1
                continue

            a = a.lower()
            b = b.lower()
            if a == b:
                left += 1
                right -= 1
            else:
                return False

        return True


if __name__ == '__main__':
    r = Solution().isPalindrome("race a car")
    print(r)
