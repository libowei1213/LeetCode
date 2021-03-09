#
# @lc app=leetcode.cn id=273 lang=python
#
# [273] 整数转换英文表示
#
# https://leetcode-cn.com/problems/integer-to-english-words/description/
#
# algorithms
# Hard (29.61%)
# Likes:    129
# Dislikes: 0
# Total Accepted:    9K
# Total Submissions: 30.1K
# Testcase Example:  '123'
#
# 将非负整数 num 转换为其对应的英文表示。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：num = 123
# 输出："One Hundred Twenty Three"
# 
# 
# 示例 2：
# 
# 
# 输入：num = 12345
# 输出："Twelve Thousand Three Hundred Forty Five"
# 
# 
# 示例 3：
# 
# 
# 输入：num = 1234567
# 输出："One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
# 
# 
# 示例 4：
# 
# 
# 输入：num = 1234567891
# 输出："One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven
# Thousand Eight Hundred Ninety One"
# 
# 
# 
# 
# 提示：
# 
# 
# 0 
# 
# 
#

# @lc code=start

num_dict = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine",
    10: "Ten",
    11: "Eleven",
    12: "Twelve",
    13: "Thirteen",
    14: "Fourteen",
    15: "Fifteen",
    16: "Sixteen",
    17: "Seventeen",
    18: "Eighteen",
    19: "Nineteen",
    20: "Twenty",
    30: "Thirty",
    40: "Forty",
    50: "Fifty",
    60: "Sixty",
    70: "Seventy",
    80: "Eighty",
    90: "Ninety"
}

# for num < 1000
def print_hundred(num):
    strs = []

    if num == 0:
        return []
    elif num <= 20:
        return [num_dict[num]]
    elif num < 100:
        strs.append(num_dict[num // 10 * 10])
        if num % 10:
            strs.append(num_dict[num % 10])
    elif num < 1000:
        strs.append(num_dict[num // 100])
        strs.append("Hundred")
        if num - num // 100 * 100:
            strs += print_hundred(num - num // 100 * 100)

    return strs

# for num < 1,000,000
def print_thousand(num):
    strs = []
    strs += print_hundred(num // 1000)
    if strs:
        strs.append("Thousand")
    if num - num // 1000 * 1000:
        strs += print_hundred(num - num // 1000 * 1000)
    return strs

def print_millon(num):
    strs = []
    strs += print_hundred(num // 1000000)
    if strs:
        strs.append("Million")
    if num - num // 1000000 * 1000000:
        strs += print_thousand(num - num // 1000000 * 1000000)
    return strs

def print_billion(num):
    strs = []
    strs += print_hundred(num // 1000000000)
    if strs:
        strs.append("Billion")
    if num - num // 1000000000 * 1000000000:
        strs += print_millon(num - num // 1000000000 * 1000000000)
    return strs

        

class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """

        #2,147,483,647

        if num == 0:
            return "Zero"

        if num < 1000:
            strs = print_hundred(num)
        elif num < 1000000:
            strs = print_thousand(num)
        elif num < 1000000000:
            strs = print_millon(num)
        else:
            strs = print_billion(num)
        print(strs)
        return " ".join([x for x in strs if x])


# @lc code=end

