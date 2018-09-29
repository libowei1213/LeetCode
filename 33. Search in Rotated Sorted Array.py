class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums == []:
            return -1

        if len(nums) == 1:
            if target == nums[0]:
                return 0
            else:
                return -1

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # mid之右为升序
            elif nums[mid] < nums[right]:
                # 查找数 在 (mid,right] 之间
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                # 其他情况，查找另一半
                else:
                    right = mid - 1
            # mid以左为升序
            else:
                # 查找数在[left,mid)之间
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


if __name__ == '__main__':
    r = Solution().search([4, 5, 6, 7, 0, 1, 2], 0)
    print(r)
