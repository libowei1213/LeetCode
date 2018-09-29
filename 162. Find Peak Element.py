import math


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        left, right = 1, len(nums) - 2

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid

            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] > nums[mid + 1]:
                right = mid - 1

        if nums[0] > nums[-1]:
            return 0
        else:
            return len(nums) - 1


r = Solution().findPeakElement([3, 2, 1])
print(r)
