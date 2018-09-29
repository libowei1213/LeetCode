class Solution:
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        sum_of_A = sum(A)
        sum_of_B = sum(B)

        target = (sum_of_A - sum_of_B) // 2

        if len(A) <= len(B):
            hash_B = dict([(x, 0) for x in B])

            for a in A:
                if a - target in hash_B:
                    return [a, a - target]

        else:
            hash_A = dict([(x, 0) for x in A])

            for b in B:
                if b + target in hash_A:
                    return [b + target,b]








if __name__ == '__main__':

    r = Solution().fairCandySwap([1,1],[2,2])
    print(r)
