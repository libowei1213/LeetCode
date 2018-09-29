class Solution:

    def find_bigger(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if mid > 0 and nums[mid - 1] <= target and nums[mid] > target:
                return mid

            elif mid < len(nums) - 1 and nums[mid] <= target and nums[mid + 1] > target:
                return mid + 1

            elif nums[mid] <= target:
                left = mid + 1

            elif nums[mid] > target:
                right = mid - 1

    def advantageCount(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """

        if not A or not B:
            return []

        A = sorted(A)

        result = []

        for num in B:
            if num >= A[-1] or num < A[0]:
                result.append(A.pop(0))
            else:
                index = self.find_bigger(A, num)
                result.append(A.pop(index))

        return result


if __name__ == '__main__':
    A = [12, 24, 8, 32]
    B = [13, 25, 32, 11]

    r = Solution().advantageCount(A, B)
    print(r)
