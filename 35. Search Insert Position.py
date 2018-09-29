class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left = 0
        right = len(nums) - 1
        last_check_index = 0

        while (left <= right):

            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
                last_check_index = mid
            else:
                last_check_index = mid + 1
                left = mid + 1

        return last_check_index


if __name__ == '__main__':
    nums = []

    r = Solution().searchInsert(nums, 1)
    print(r)
