def dfs(nums, remaining, sums, target, answers):
    if sums == target:
        answers.append(nums)
        return
    if sums > target:
        return

    for i, num in enumerate(remaining):
        dfs(nums + [num], remaining[i:], sums + num, target, answers)


class Solution:

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        ans=[]
        dfs([],candidates,0,target,ans)
        return ans


if __name__ == '__main__':

    r = Solution().combinationSum([2,3,5],8)
    print(r)