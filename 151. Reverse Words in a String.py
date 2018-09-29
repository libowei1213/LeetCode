class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        s = s.split()
        size = len(s)
        return " ".join([s[size - i - 1] for i in range(size)])


if __name__ == '__main__':
    r = Solution().reverseWords("the sky is blue")
    print(r)
