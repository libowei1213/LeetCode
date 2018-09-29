class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        even = []
        odd = []

        for num in A:
            if num & 1 == 1:
                odd.append(num)
            else:
                even.append(num)

        return even + odd
