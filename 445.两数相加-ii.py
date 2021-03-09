#
# @lc app=leetcode.cn id=445 lang=python
#
# [445] 两数相加 II
#
# https://leetcode-cn.com/problems/add-two-numbers-ii/description/
#
# algorithms
# Medium (58.22%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    61.6K
# Total Submissions: 105.6K
# Testcase Example:  '[7,2,4,3]\n[5,6,4]'
#
# 给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
# 
# 你可以假设除了数字 0 之外，这两个数字都不会以零开头。
# 
# 
# 
# 进阶：
# 
# 如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
# 
# 
# 
# 示例：
# 
# 输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 8 -> 0 -> 7
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        a = []
        while l1:
            a.append(l1.val)
            l1 = l1.next
        b = []
        while l2:
            b.append(l2.val)
            l2 = l2.next

        a = a[::-1]
        b = b[::-1]

        if len(a) > len(b):
            b.extend([0] * (len(a) - len(b)))
        elif len(a) < len(b):
            a.extend([0] * (len(b) - len(a)))

      
        assert len(a) == len(b)

        add_one = 0
        for i in range(len(a)):
            temp = a[i] + b[i] + add_one
            if temp >= 10:
                temp %= 10
                add_one = 1
            else:
                add_one = 0
            a[i] = temp
        
        if add_one:
            a.append(1)

        list_nodes = [ListNode(val) for val in a]
        for i in range(len(list_nodes) - 1, 0, -1):
            list_nodes[i].next = list_nodes[i - 1]
            
        return list_nodes[-1]

        
# @lc code=end

