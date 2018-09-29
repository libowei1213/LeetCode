def dfs(nums, sums, candidates, target, ans):
    if sums > target:
        return

    if sums == target:
        ans[tuple(nums)] = True
        return

    for i in range(len(candidates)):
        dfs(nums + [candidates[i]], sums + candidates[i], candidates[i + 1:], target, ans)


class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = {}
        dfs([], 0, candidates, target, ans)

        return [list(x) for x in ans.keys()]