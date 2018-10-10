class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """


        left = []
        right = []

        for num in A:
            if not left:
                left.append(num)
            else:
                left.append(max(num,left[-1]))

        for num in A[::-1]:
            if not right:
                right.insert(0,num)
            else:
                right.insert(0,min(num,right[0]))


        for i in range(len(left)):
            if left[i]<=right[i+1]:
                return i+1


if __name__ == '__main__':

    r = Solution().partitionDisjoint([1,1,1,0,6,12])
    print(r)