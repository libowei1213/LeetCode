class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        size = len(s)
        if size == 0:
            return 0
        elif size == 1:
            if s == "0":
                return 0
            else:
                return 1

        dp = [0] * size
        if s[0] == "0":
            dp[0] = 0
        else:
            dp[0] = 1

        for i in range(1, size):
            a = int(s[i])
            b = int(s[i - 1:i + 1])

            if (a >= 1 and a <= 9):
                dp[i] += dp[i - 1]
            if (b >= 10 and b <= 26):
                if i >= 2:
                    dp[i] += dp[i - 2]
                else:
                    dp[i] += 1
        return dp[-1]


if __name__ == '__main__':
    r = Solution().numDecodings("01")
    print(r)
