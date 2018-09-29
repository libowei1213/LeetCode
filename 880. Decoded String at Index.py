class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        if not S or K <= 0:
            return ""

        n = 0

        for i, s in enumerate(S):
            if s.isdigit():
                n *= int(s)
            else:
                n += 1
            if n >= K:
                break

        for j in range(i, -1, -1):
            if S[j].isdigit():
                n //= int(S[j])
                K %= n
            else:
                if K == n or K == 0:
                    return S[j]
                else:
                    n -= 1