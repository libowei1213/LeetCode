class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """

        if not A:
            return False

        increasing = A[0] >= A[-1]

        for i in range(len(A) - 1):
            if increasing and A[i] < A[i + 1]:
                return False
            if not increasing and A[i] > A[i + 1]:
                return False

        return True
