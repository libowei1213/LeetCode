#
# @lc app=leetcode.cn id=1006 lang=python3
#
# [1006] 笨阶乘
#

# @lc code=start
class Solution:
    def clumsy(self, N: int) -> int:
        

        stack = [N]
        signals = ["*","/","+","-"]

        nums = [ x for x in range(N-1,0,-1)]



        for i in range(len(nums)):
            sign = signals[i%len(signals)]
            if sign == "+":
                stack.append(nums[i])
            elif sign == "-":
                stack.append(-nums[i])
            elif sign == "*":
                stack[-1] *= nums[i]
            elif sign == "/":
                stack[-1] = int(stack[-1]/nums[i])

        return sum(stack)


# @lc code=end

