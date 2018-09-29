from collections import defaultdict


class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        a = len(word1)
        b = len(word2)

        dp = defaultdict(int)

        for i in range(len(word1)):
            dp[(i, -1)] = i + 1
        for i in range(len(word2)):
            dp[(-1, i)] = i + 1

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    dp[(i, j)] = dp[(i - 1, j - 1)]
                else:
                    dp[(i, j)] = min(dp[(i - 1, j)], dp[(i, j - 1)], dp[(i - 1, j - 1)]) + 1

        return dp[(a-1,b-1)]


if __name__ == '__main__':
    r = Solution().minDistance("intention", "execution")
    print(r)
