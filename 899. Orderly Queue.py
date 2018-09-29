class Solution:
    def orderlyQueue(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        if K > 1:
            return "".join(sorted(S))

        min_string = S

        for i in range(len(S)):
            S = S[1:] + S[0]
            if S < min_string:
                min_string = S

        return min_string


if __name__ == '__main__':
    r = Solution().orderlyQueue("kikc", 1)
    print(r)
