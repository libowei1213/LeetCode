class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1

        l = len(nums)

        for i in range(len(nums)):
            if nums[i] <= 0 or nums[i] >= l + 1:
                nums[i] = 0

        nums.append(0)
        nums.append(0)
        for i in range(len(nums)):
            value = nums[i]
            value %= (l + 1)
            nums[value] -= (l + 1)

        print(nums)

        for i in range(len(nums)):
            if nums[i] >= 0:
                return i


if __name__ == '__main__':
    r = Solution().firstMissingPositive([1])
    print(r)
