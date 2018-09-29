class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """

        nums = [1] * n

        num = 2
        while num < n // 2 + 1:
            temp = num + num
            while temp < n:
                nums[temp] = 0
                temp += num

            # 找下一个 num
            num += 1
            while num < n // 2 + 1 and nums[num] == 0:
                num += 1

        return sum(nums[2:n])