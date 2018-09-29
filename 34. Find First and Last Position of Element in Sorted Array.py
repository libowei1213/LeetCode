class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        if not nums:
            return [-1, -1]

        left, right = 0, len(nums) - 1
        start, end = -1, -1

        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        start = left

        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2 + 1
            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid

        end = left

        return [start, end] if nums[start] == target and nums[end] == target else [-1, -1]


if __name__ == '__main__':
    r = Solution().searchRange([5, 7, 7, 8, 8, 10], 8)
    print(r)
