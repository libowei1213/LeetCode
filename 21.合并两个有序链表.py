#
# @lc app=leetcode.cn id=21 lang=python
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (65.47%)
# Likes:    1588
# Dislikes: 0
# Total Accepted:    493.4K
# Total Submissions: 753.1K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：l1 = [1,2,4], l2 = [1,3,4]
# 输出：[1,1,2,3,4,4]
# 
# 
# 示例 2：
# 
# 
# 输入：l1 = [], l2 = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：l1 = [], l2 = [0]
# 输出：[0]
# 
# 
# 
# 
# 提示：
# 
# 
# 两个链表的节点数目范围是 [0, 50]
# -100 
# l1 和 l2 均按 非递减顺序 排列
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """


        head = ListNode()

        node = head

        # while l1 or l2:
        #     val = 0
        #     if l1 and l2:
        #         if l1.val <= l2.val:
        #             val = l1.val
        #             l1 = l1.next
        #         else:
        #             val = l2.val
        #             l2 = l2.next
        #     else:
        #         if l1:
        #             val = l1.val
        #             l1 = l1.next
        #         if l2:
        #             val = l2.val
        #             l2 = l2.next
        #     node.next = ListNode(val)
        #     node = node.next


        while l1 or l2:

            if l1 and l2:

                if l1.val <= l2.val:
                    node.next = l1
                    l1 = l1.next
                else:
                    node.next = l2
                    l2 = l2.next

            else:
                if l1:
                    node.next = l1
                    break
                if l2:
                    node.next = l2
                    break
            node = node.next



        
        return head.next

                


# @lc code=end

