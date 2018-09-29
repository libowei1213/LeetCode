class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return None

        l = len(nums)

        dp_max = [nums[0]] * l
        dp_min = [nums[0]] * l

        for i, num in enumerate(nums):
            if i == 0:
                continue

            dp_max[i] = max(dp_max[i - 1] * num, dp_min[i - 1] * num, num)
            dp_min[i] = min(dp_max[i - 1] * num, dp_min[i - 1] * num, num)


        return max(dp_max)


if __name__ == '__main__':
    r = Solution().maxProduct([-2,0,-1])
    print(r)
