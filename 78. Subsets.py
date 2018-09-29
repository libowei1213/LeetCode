def dfs(subset, nums, answers):
    answers.append(subset)
    for i in range(len(nums)):
        dfs(subset + [nums[i]], nums[i + 1:], answers)


class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answers = []
        dfs([], nums, answers)
        return answers


if __name__ == '__main__':
    r = Solution().subsets([1, 2, 3])
    print(r)
