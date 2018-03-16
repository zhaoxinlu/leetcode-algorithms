# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-09
算法思想： 排序的链表转换成二叉排序树
"""
"""
Definition of ListNode
"""
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param: head: The first node of linked list.
    @return: a tree node
    """
    def sortedListToBST(self, head):
        # write your code here
        if head == None:
            return None

        if head.next == None:
            return TreeNode(head.val)

        midPreOneNode = self.middlePreOneList(head)
        midNode = midPreOneNode.next
        midPreOneNode.next = None

        root = TreeNode(midNode.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(midNode.next)

        return root

    def middlePreOneList(self, head):
        """
        寻中间节点的前一个节点
        :param head:
        :return:
        """
        dummy = ListNode(0)
        dummy.next = head
        slow, fast = dummy, head

        while fast != None and fast.next != None:
            #### 注意
            slow = slow.next
            fast = fast.next.next

        return slow

if __name__ == '__main__':
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    print Solution().sortedListToBST(head).left.left.val