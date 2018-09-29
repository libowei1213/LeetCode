class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        base=[[1],[1,1]]

        if numRows<=2:
            return base[:numRows]

        for _ in range(3,numRows+1):

            row = []
            for i in range(len(base[-1])-1):
                row.append(base[-1][i]+base[-1][i+1])
            row.insert(0,1)
            row.append(1)
            base.append(row)


        return base


if __name__ == '__main__':

    r = Solution().generate(5)
    print(r)