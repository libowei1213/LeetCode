class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        result = set()
        nums.sort()

        for i in range(len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                left = j + 1
                right = len(nums) - 1

                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
                    else:
                        result.add((nums[i], nums[j], nums[left], nums[right]))
                        left += 1
                        right -= 1

        return [list(r) for r in result]


if __name__ == '__main__':
    testcase = [1, 0, -1, 0, -2, 2]
    r = Solution()
    s = r.fourSum(testcase, 0)
    print(s)
