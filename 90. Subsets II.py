def serialize(list):
    return "[%s]" % ",".join([str(x) for x in list])


def dfs(subset, nums, answers):
    answers.add(serialize(subset))
    for i in range(len(nums)):
        dfs(subset + [nums[i]], nums[i + 1:], answers)


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()

        answers = set()
        dfs([], nums, answers)
        return [eval(x) for x in answers]


if __name__ == '__main__':
    r = Solution().subsetsWithDup([4, 4, 4, 1, 4])
    print(r)
