class Solution:

    def judge(self, a, b):
        a_str = str(a)
        b_str = str(b)

        a_str = sorted(a_str)
        b_str = sorted(b_str)

        return a_str == b_str

    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """

        N_len = len(str(N))

        i = 1
        while True:
            i_len = len(str(i))
            if i_len < N_len:
                i <<= 1
                continue
            elif i_len == N_len:
                if self.judge(i, N):
                    return True
                else:
                    i <<= 1
                    continue
            else:
                break

        return False


if __name__ == '__main__':
    r = Solution().reorderedPowerOf2(46)
    print(r)
