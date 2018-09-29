class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if nums == []:
            return False

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # 左边为升序
            elif nums[mid] > nums[left]:
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                # 其他情况，查找另一半
                else:
                    left = mid + 1
            # 右边为升序
            elif nums[mid] < nums[left]:
                # 查找数在[left,mid)之间
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return False


r = Solution().search([3,1,1], 3)
print(r)
