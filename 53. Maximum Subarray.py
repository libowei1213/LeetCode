class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if nums == []:
            return 0

        max_array = [x for x in nums]

        value = max_array[0]
        for i in range(1, len(nums)):
            max_array[i] = max(nums[i] + max_array[i - 1], nums[i])
            value = max_array[i] if max_array[i] > value else value

        return value


if __name__ == '__main__':
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    r = Solution().maxSubArray(arr)
    print(r)
