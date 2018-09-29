class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        if rowIndex==0:
            return [1]
        if rowIndex==1:
            return [1,1]

        last = [1,1]
        for _ in range(2, rowIndex + 1):

            row = []
            for i in range(len(last) - 1):
                row.append(last[i] + last[i + 1])
            row.insert(0, 1)
            row.append(1)
            last=row

        return last

if __name__ == '__main__':

    r = Solution().getRow(3)
    print(r)