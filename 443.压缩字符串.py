#
# @lc app=leetcode.cn id=443 lang=python
#
# [443] 压缩字符串
#
# https://leetcode-cn.com/problems/string-compression/description/
#
# algorithms
# Medium (41.49%)
# Likes:    161
# Dislikes: 0
# Total Accepted:    25.5K
# Total Submissions: 61.4K
# Testcase Example:  '["a","a","b","b","c","c","c"]'
#
# 给定一组字符，使用原地算法将其压缩。
# 
# 压缩后的长度必须始终小于或等于原数组长度。
# 
# 数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。
# 
# 在完成原地修改输入数组后，返回数组的新长度。
# 
# 
# 
# 进阶：
# 你能否仅使用O(1) 空间解决问题？
# 
# 
# 
# 示例 1：
# 
# 输入：
# ["a","a","b","b","c","c","c"]
# 
# 输出：
# 返回 6 ，输入数组的前 6 个字符应该是：["a","2","b","2","c","3"]
# 
# 说明：
# "aa" 被 "a2" 替代。"bb" 被 "b2" 替代。"ccc" 被 "c3" 替代。
# 
# 
# 示例 2：
# 
# 输入：
# ["a"]
# 
# 输出：
# 返回 1 ，输入数组的前 1 个字符应该是：["a"]
# 
# 解释：
# 没有任何字符串被替代。
# 
# 
# 示例 3：
# 
# 输入：
# ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
# 
# 输出：
# 返回 4 ，输入数组的前4个字符应该是：["a","b","1","2"]。
# 
# 解释：
# 由于字符 "a" 不重复，所以不会被压缩。"bbbbbbbbbbbb" 被 “b12” 替代。
# 注意每个数字在数组中都有它自己的位置。
# 
# 
# 
# 
# 提示：
# 
# 
# 所有字符都有一个ASCII值在[35, 126]区间内。
# 1 <= len(chars) <= 1000。
# 
# 
#

# @lc code=start
class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        length = len(chars)

        last_char = ''
        size = 0


        for i in range(length-1, -1, -1):
            if chars[i] != last_char:
                
                temp = [last_char]
                if size > 1:
                    temp+=[x for x in str(size)]
                chars[i + 1:i + 1 + size] = temp
                
                last_char = chars[i]
                size = 1 

            else:
                size += 1
        else:

            if size >= 1:
                temp = [last_char]
                if size > 1:
                    temp+=[x for x in str(size)]
                chars[0:size] = temp

        
        chars.pop(-1)


        return len(chars)

        
# @lc code=end

