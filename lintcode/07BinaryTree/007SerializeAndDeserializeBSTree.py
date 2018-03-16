# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-03-10
算法思想： 二叉树的序列化和反序列化--BFS遍历
"""
"""
Definition of TreeNode:
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        # write your code here
        if root == None:
            return "{}"

        Nodes = [root]
        index = 0
        while index < len(Nodes):
            if Nodes[index] != None:
                Nodes.append(Nodes[index].left)
                Nodes.append(Nodes[index].right)
            index += 1

        while Nodes[-1] == None:
            Nodes.pop()

        nodeVals = []
        for node in Nodes:
            if node:
                nodeVals.append(str(node.val))
            else:
                nodeVals.append('#')

        return '{%s}' % ','.join(nodeVals)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        # write your code here
        data = data.strip('\n')
        if data == "{}":
            return None

        vals = data[1:-1].split(',')
        # ['3', '9', '20', '#', '#', '15', '7']
        root = TreeNode(int(vals[0]))
        nodes = [root]
        index = 0
        isLeftChild = 1
        for val in vals[1:]:
            if val != '#':
                tmpNode = TreeNode(int(val))
                if isLeftChild == 1:
                    nodes[index].left = tmpNode
                else:
                    nodes[index].right = tmpNode
                nodes.append(tmpNode)

            if isLeftChild == 0:
                index += 1
            isLeftChild = not isLeftChild

        return root

if __name__ == '__main__':
    root = TreeNode(3)
    node1 = TreeNode(9)
    node2 = TreeNode(20)
    node3 = TreeNode(15)
    node4 = TreeNode(7)
    root.left = node1
    root.right = node2
    node2.left = node3
    node2.right = node4

    s = Solution().serialize(root)
    # {3,9,20,#,#,15,7}
    print Solution().deserialize(s).right.left.val