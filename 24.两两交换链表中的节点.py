#
# @lc app=leetcode.cn id=24 lang=python
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (69.24%)
# Likes:    848
# Dislikes: 0
# Total Accepted:    229.6K
# Total Submissions: 331.5K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 
# 
# 
# 
# 
# 进阶：你能在不修改链表节点值的情况下解决这个问题吗?（也就是说，仅修改节点本身。）
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head:
            return None

        node = ListNode()
        p = node
        p.next = head 


        while p.next and p.next.next:

            p1 = p.next
            p2 = p1.next

            p.next = p2
            p1.next = p2.next
            p2.next = p1

            p = p1


        return node.next
        

        


# @lc code=end

