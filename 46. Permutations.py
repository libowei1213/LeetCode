def dfs(nums, left, digit, answers):
    if len(nums) == digit:
        answers.append(nums)
    for i, num in enumerate(left):
        dfs(nums + [num], left[:i] + left[i + 1:], digit, answers)


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        answers = []
        dfs([], nums, len(nums), answers)
        return answers


if __name__ == '__main__':
    r = Solution().permute([1, 2, 3])
    print(r)
