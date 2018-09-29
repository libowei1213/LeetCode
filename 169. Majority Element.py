class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        temp = None
        count = 0

        for num in nums:
            if temp == None:
                temp = num
                count = 1

            else:

                if num == temp:
                    count += 1
                elif count > 1:
                    count -= 1
                else:
                    temp = num
                    count = 1

        return temp


if __name__ == '__main__':
    r = Solution().majorityElement([3,2,3])
    print(r)