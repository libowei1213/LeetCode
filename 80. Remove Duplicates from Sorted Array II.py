class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0
        for num in nums:
            if i<2 or num > nums[i-2]:
                nums[i]=num
                i+=1

        for j in range(len(nums)-1,i-1,-1):
            del nums[j]


if __name__ == '__main__':

    list = [1,1,1,1,1,2,3,3,3,5,5,6]
    Solution().removeDuplicates(list)
    print(list)