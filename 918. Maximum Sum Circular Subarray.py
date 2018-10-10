class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        if not A:
            return None

        dp_min = []
        dp_max = []

        for i, num in enumerate(A):
            if i == 0:
                dp_min.append(num)
                dp_max.append(num)
            if i > 0:
                dp_min.append(min(num, dp_min[-1] + num))
                dp_max.append(max(num, dp_max[-1] + num))

        if sum(A) == min(dp_min):
            return max(dp_max)
        else:
            return max(sum(A) - min(dp_min), max(dp_max))


if __name__ == '__main__':
    r = Solution().maxSubarraySumCircular([-2, -3, -1])
    print(r)
