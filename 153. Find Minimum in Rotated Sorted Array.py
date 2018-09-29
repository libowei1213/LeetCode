class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:
                return nums[mid]

            # 左边升序
            if nums[mid] >= nums[left]:
                if nums[left] < nums[right]:
                    return nums[left]
                else:
                    left = mid + 1

            # 右边升序
            elif nums[mid] < nums[left]:
                right = mid - 1


if __name__ == '__main__':
    r = Solution().findMin([1,2])
    print(r)
