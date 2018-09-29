class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        if len(numbers) == 2:
            return [1, 2]

        left, right = 0, len(numbers) - 1

        while left < right:
            sum = numbers[left] + numbers[right]
            if sum == target:
                return [left + 1, right + 1]
            elif target > sum:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    r = Solution().twoSum([2, 7, 11, 15], 9)
    print(r)
