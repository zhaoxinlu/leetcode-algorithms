# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-04-10
算法思想：完全二叉树层结点连接
"""
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        """
        思路是，先用循环把右侧的所有next指针设为NULL，然后使用两个指针，一个表示当前节点，另一个表示指向当前节点的前一个节点
        然后按层，一层一层的把next指针都填充完毕。
        一开始prev指向1,cur指向2。我们填充next指针的代码放入一个循环中，分为3种情况判断
        1：当cur指针是prev的左孩子时，这个时候只需将cur->next 指向prev->right即可。然后使用cur=cur->next把cur指针移向下一个节点。
        2：当cur指针是右孩子，而且cur->next不为NULL时，这个时候就是cur是prev的右孩子，但是不在最右侧。
            这种情况只需把cur->next指向prev->next->left就可以了。然后把cur和prev都向next移动，指向下一个节点
        3：其他情况也就是cur是最右侧的节点，这时候需要判断cur是否为最后一个节点，如果是的话就退出循环;
            如果不是，则将cur和prev都指向下一层的第一个节点。
        使用了cnt表示当前是第几层，每执行到这个判断代码段的时候，我们把cnt自增，表示到下一层去。
            通过cnt的大小我们就可以通过循环找到下一层的第一个节点。
        :param root:
        :return:
        """
        if not root:
            return
        cur = root
        pre = root
        level = 0
        while cur:
            cur.next = None
            cur = cur.right
        if root.left:
            cur = root.left
        else:
            return

        while True:
            if cur == pre.left:
                cur.next = pre.right
                cur = cur.next
            elif cur == pre.right and pre.next != None:
                cur.next = pre.next.left
                cur = cur.next
                pre = pre.next
            else:
                if not cur.left:
                    break
                else:
                    level += 1
                    pre = root
                    for i in range(level):
                        pre = pre.left
                    cur = pre.left

        return root