class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """

        distance = 0
        last_index = None

        i = 0
        while N:
            if N & 1:
                if last_index != None:
                    if i - last_index > distance:
                        distance = i - last_index

                last_index = i

            N >>= 1
            i += 1

        return distance


if __name__ == '__main__':
    r = Solution().binaryGap(22)
    print(r)
