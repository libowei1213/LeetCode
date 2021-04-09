#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:


        if not s:
            return True

        if s.isspace():
            return True

        s = s.lower()
        s = "".join([ char for char in s if char.isdigit() or char.isalpha()])
        return s==s[::-1]


# @lc code=end

