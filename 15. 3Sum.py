# coding=utf-8

class Solution:

    # Accept
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return [list(r) for r in result]

    # Time Limit Exceeded
    def threeSum2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = set()
        nums.sort()

        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):

                if -(nums[i] + nums[j]) in nums[j + 1:]:
                    result.add((nums[i], nums[j], -(nums[i] + nums[j])))

        return [list(r) for r in result]


if __name__ == '__main__':
    testcase = [-1, 0, 1, 2, -1, -4]
    r = Solution()
    s = r.threeSum(testcase)
    print(s)
