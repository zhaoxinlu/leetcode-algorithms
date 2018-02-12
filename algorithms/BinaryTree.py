# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-30
Function: 二叉树相关常用知识点
"""
class BTNode(object):
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild

class BTree(object):
    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        if self.root == None:
            return True
        return False

    def preOrderReverse(self, root):
        """
        递归实现二叉树的前序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        preVal = [root.val]
        left = self.preOrderReverse(root.lchild)
        right = self.preOrderReverse(root.rchild)

        return preVal+left+right

    def preOrderNonreverse(self, root):
        """
        非递归（迭代）实现二叉树的前序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        nodes = [root]
        preVal = []

        while nodes:
            curNode = nodes.pop()
            preVal.append(curNode.val)

            if curNode.rchild:
                nodes.append(curNode.rchild)

            if curNode.lchild:
                nodes.append(curNode.lchild)

        return preVal

    def inOrderReverse(self, root):
        """
        递归实现二叉树的中序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        inVal = [root.val]
        left = self.inOrderReverse(root.lchild)
        right = self.inOrderReverse(root.rchild)

        return left+inVal+right

    def inOrderNonreverse(self, root):
        """
        非递归（迭代）实现二叉树的中序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        nodes = []
        inVal = []
        curNode = root

        while nodes or curNode:
            while curNode:
                nodes.append(curNode)
                curNode = curNode.lchild

            curNode = nodes.pop()
            inVal.append(curNode.val)
            curNode = curNode.rchild

        return inVal

    def postOrderReverse(self, root):
        """
        递归实现二叉树的后序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        postVal = [root.val]
        left = self.postOrderReverse(root.lchild)
        right = self.postOrderReverse(root.rchild)

        return left+right+postVal

    def levelOrder(self, root):
        """
        二叉树的层序遍历
        :param root:
        :return:
        """
        if root == None:
            return []

        nodes = [root]
        levelVal = [root.val]

        while nodes != []:
            curNode = nodes.pop(0)

            if curNode.lchild != None:
                nodes.append(curNode.lchild)
                levelVal.append(curNode.lchild.val)

            if curNode.rchild != None:
                nodes.append(curNode.rchild)
                levelVal.append(curNode.rchild.val)

        return levelVal

    def levelOrderLayer(self, root):
        """
        分行层次打印二叉树
        :param root:
        :return:
        """
        if root == None:
            return

        nodes = [root]
        numOfToBePrintedNode = 1 # 该层待打印节点个数
        numOfLevelNode = 0 # 下一层节点个数
        levelVal = [] # 存放每层节点的元素value

        while nodes != []:
            curNode = nodes.pop(0)
            numOfToBePrintedNode -= 1
            levelVal.append(curNode.val)

            if curNode.lchild != None:
                nodes.append(curNode.lchild)
                numOfLevelNode += 1

            if curNode.rchild != None:
                nodes.append(curNode.rchild)
                numOfLevelNode += 1

            if numOfToBePrintedNode == 0:
                print levelVal
                numOfToBePrintedNode = numOfLevelNode
                numOfLevelNode = 0
                del levelVal[:] # 清空每一层的元素

    def zigzagOrder(self, root):
        """
        之字型分行层次打印二叉树
        :param root:
        :return:
        """
        if root == None:
            return []

        # zigzagVal = []
        flag = 1
        nodes = [root]

        while nodes != []:
            nlNode = []
            resVal = []

            for node in nodes:
                if node.lchild != None:
                    nlNode.append(node.lchild)
                if node.rchild != None:
                    nlNode.append(node.rchild)
                resVal.append(node.val)

            if flag == 0:
                #zigzagVal.append(resVal[::-1])
                print resVal[::-1]
                flag = 1
            else:
                #zigzagVal.append(resVal)
                print resVal
                flag = 0

            nodes = nlNode

        #return zigzagVal

    def maxDepth(self, root):
        """
        递归实现求二叉树的最大深度
        :param root:
        :return:
        """
        if root == None:
            return 0

        left = self.maxDepth(root.lchild)
        right = self.maxDepth(root.rchild)

        return max(left, right) + 1

    def numOfTreeNode(self, root):
        """
        递归实现求二叉树的节点数目
        :param root:
        :return:
        """
        if root == None:
            return 0

        left = self.numOfTreeNode(root.lchild)
        right = self.numOfTreeNode(root.rchild)

        return left + right + 1

    def numOfTreeNoChildNode(self, root):
        """
        递归实现求二叉树中叶子节点的个数
        :param root:
        :return:
        """
        if root == None:
            return 0

        if root.lchild == None and root.rchild == None:
            return 1

        return self.numOfTreeNoChildNode(root.lchild) + self.numOfTreeNoChildNode(root.rchild)

    def numOfTreeKLevelNode(self, root, k):
        """
        递归实现求二叉树中第k层节点的个数
        :param root:
        :param k:
        :return:
        """
        if root == None or k < 1:
            return 0

        if k == 1:
            return 1

        left = self.numOfTreeKLevelNode(root.lchild, k-1)
        right = self.numOfTreeKLevelNode(root.rchild, k-1)

        return left + right

    def maxDepth2(self, root):
        """
        辅助函数，树的最大深度
        :param root:
        :return:
        """
        if root == None:
            return 0

        left = self.maxDepth2(root.lchild)
        right = self.maxDepth2(root.rchild)

        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1

        return max(left, right) + 1

    def isBalancedBTree(self, root):
        """
        判断二叉树是不是平衡二叉树
        :param root:
        :return:
        """
        return self.maxDepth2(root) != -1

    def isSameTwoTree(self, root1, root2):
        """
        判断两棵二叉树是否完全相同
        :param root1:
        :param root2:
        :return:
        """
        if root1 == None and root2 == None:
            return True

        if root1 != None and root2 != None and root1.val == root2.val:
            return self.isSameTwoTree(root1.lchild, root2.lchild) and self.isSameTwoTree(root1.rchild, root2.rchild)

        return False
    
    def isMirrorTwoTree(self, root1, root2):
        """
        判断两棵二叉树是否互为镜像
        :param root1: 
        :param root2: 
        :return: 
        """
        if root1 == None and root2 == None:
            return True

        if root1 != None and root2 != None and root1.val == root2.val:
            return self.isMirrorTwoTree(root1.lchild, root2.rchild) and self.isMirrorTwoTree(root1.rchild, root2.lchild)

        return False

    def treeMirror(self, root):
        """
        递归实现二叉树的镜像，返回镜像二叉树的根节点
        :param root:
        :return:
        """
        if root == None:
            return root

        if root.lchild == None and root.rchild == None:
            return root

        tmpNode = root.lchild
        root.lchild = root.rchild
        root.rchild = tmpNode

        if root.lchild:
            self.treeMirror(root.lchild)

        if root.rchild:
            self.treeMirror(root.rchild)

        return root

    def isSymmetricalTree(self, root):
        """
        判断一棵二叉树是不是对称的(递归判断根节点左右子树是否镜像)
        :param root:
        :return:
        """
        if not root:
            return True

        if not root.lchild and root.rchild:
            return False

        if not root.rchild and root.lchild:
            return False

        return self.isMirrorTwoTree(root.lchild, root.rchild)

    def findCertainValuePathOfBTree(self, root, value):
        """
        Offer034二叉树中和为某一值的所有路径
        :param root:
        :param value:
        :return:
        """
        if root == None:
            return []

        path = []
        curSum = 0
        self.findOneCerValPathOfTree(root, value, path, curSum)

    def findOneCerValPathOfTree(self, root, value, path, curSum):
        """
        逐条输出二叉树中和为某一值的路径
        :param root:
        :param value:
        :param path:
        :param curSum:
        :return:
        """
        curSum += root.val
        path.append(root.val)

        isLeaf = (root.lchild == None and root.rchild == None)
        if curSum == value and isLeaf:
            print path

        if root.lchild != None:
            self.findOneCerValPathOfTree(root.lchild, value, path, curSum)
        if root.rchild != None:
            self.findOneCerValPathOfTree(root.rchild, value, path, curSum)

        path.pop()


if __name__ == '__main__':
    # 用例测试功能函数是否正确
    print "构建第一棵二叉树中..."
    root1 = BTNode(8)
    bt2 = BTNode(6)
    bt3 = BTNode(10)
    bt4 = BTNode(5)
    bt5 = BTNode(7)
    bt6 = BTNode(9)
    bt7 = BTNode(11)
    root1.lchild = bt2
    root1.rchild = bt3
    bt2.lchild = bt4
    bt2.rchild = bt5
    bt3.lchild = bt6
    bt3.rchild = bt7
    BTree1 = BTree(root1)
    print "第一棵二叉树构建成功！"

    print "构建第二棵二叉树中..."
    root2 = BTNode(8)
    bt22 = BTNode(6)
    bt33 = BTNode(6)
    bt44 = BTNode(5)
    bt55 = BTNode(7)
    bt66 = BTNode(7)
    bt77 = BTNode(5)
    root2.lchild = bt22
    root2.rchild = bt33
    bt22.lchild = bt44
    bt22.rchild = bt55
    bt33.lchild = bt66
    bt33.rchild = bt77
    BTree2 = BTree(root2)
    print "第二棵二叉树构建成功！"

    print "第一棵二叉树递归---二叉树的前序遍历:", BTree1.preOrderReverse(BTree1.root)
    print "第一棵二叉树非递归---二叉树的前序遍历:", BTree1.preOrderNonreverse(BTree1.root)
    print "第一棵二叉树递归---二叉树的中序遍历:", BTree1.inOrderReverse(BTree1.root)
    print "第一棵二叉树非递归---二叉树的中序遍历:", BTree1.inOrderNonreverse(BTree1.root)
    print "第一棵二叉树递归---二叉树的后序遍历:", BTree1.postOrderReverse(BTree1.root)
    print "第一棵二叉树的层序遍历:", BTree1.levelOrder(BTree1.root)
    print "分行层次打印第一棵二叉树:"
    BTree1.levelOrderLayer(BTree1.root)
    print "之字型分行层次打印第一棵二叉树:"
    BTree1.zigzagOrder(BTree1.root)
    print "第二棵二叉树中和为value=19的路径为:"
    BTree2.findCertainValuePathOfBTree(BTree2.root, value=19)

    print "第一棵二叉树的最大深度是:", BTree1.maxDepth(BTree1.root)
    print "第一棵二叉树的节点个数是:", BTree1.numOfTreeNode(BTree1.root)
    print "第一棵二叉树的叶子节点个数是:", BTree1.numOfTreeNoChildNode(BTree1.root)
    print "第一棵二叉树第2层的节点数目是:", BTree1.numOfTreeKLevelNode(BTree1.root, 2)
    print "第一棵二叉树是不是平衡二叉树:", BTree1.isBalancedBTree(BTree1.root)
    print "第一棵二叉树是不是对称二叉树:", BTree1.isSymmetricalTree(BTree1.root)
    print "第二棵二叉树是不是对称二叉树:", BTree2.isSymmetricalTree(BTree2.root)
    print "两棵二叉树是否完全相同:", BTree().isSameTwoTree(BTree1.root, BTree2.root)
    print "两棵二叉树是否互为镜像:", BTree().isMirrorTwoTree(BTree1.root, BTree2.root)
    print "第二棵二叉树是不是对称二叉树:", BTree2.isSymmetricalTree(BTree2.root)
    BTree3 = BTree()
    BTree3.root = BTree1.treeMirror(BTree1.root) # 原二叉树亦镜像
    print "第一棵二叉树的镜像二叉树的根节点右孩子的值为(=6即为成功):", BTree3.root.rchild.val == 6