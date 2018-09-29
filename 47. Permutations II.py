def dfs(numbers, candidates, ans):
    if candidates == []:
        ans[tuple(numbers)] = True

    for i, num in enumerate(candidates):
        dfs(numbers + [num], candidates[:i] + candidates[i + 1:], ans)


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        ans = {}
        dfs([], nums, ans)
        return [list(x) for x in ans.keys()]


if __name__ == '__main__':
    r = Solution().permuteUnique([1, 1, 2])
    print(r)
