class Solution(object):
    def longestPalindrome(self, s):

        size = len(s)

        if size == 0:
            return ""

        if size == 1:
            return s

        maxlen = 0
        maxrange = (0, 0)

        for i in range(1, size):

            nowrange = [0, 0]

            if s[i] == s[i - 1]:
                left = i - 1
                right = i

                while left >= 0 and right < size:
                    if s[left] == s[right]:
                        nowrange = [left, right]
                        left -= 1
                        right += 1
                    else:
                        break

                if nowrange[1] - nowrange[0] > maxrange[1] - maxrange[0]:
                    maxrange = nowrange

            left = i - 1
            right = i + 1

            while left >= 0 and right < size:
                if s[left] == s[right]:
                    nowrange = [left, right]
                    left -= 1
                    right += 1
                else:
                    break

            if nowrange[1] - nowrange[0] > maxrange[1] - maxrange[0]:
                maxrange = nowrange

        return s[maxrange[0]:maxrange[1] + 1]
