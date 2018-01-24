# -*- coding: utf-8 -*-
"""
构造一颗二叉排序树的目的，往往不是为了排序，而是为了提高查找和插入删除关键字的速度。

二叉排序树的操作：
    查找：对比节点的值和关键字，相等则表明找到了；小了则往节点的左子树去找，大了则往右子树去找，这么递归下去，最后返回布尔值或找到的节点。
    插入：从根节点开始逐个与关键字进行对比，小了去左边，大了去右边，碰到子树为空的情况就将新的节点链接。
    删除：如果要删除的节点是叶子，直接删；如果只有左子树或只有右子树，则删除节点后，将子树链接到父节点即可；
         如果同时有左右子树，则可以将二叉排序树进行中序遍历，取将要被删除的节点的前驱或者后继节点替代这个被删除的节点的位置。

总结：
    二叉排序树以链式进行存储，保持了链接结构在插入和删除操作上的优点。
    在极端情况下，查询次数为1，但最大操作次数不会超过树的深度。也就是说，二叉排序树的查找性能取决于二叉排序树的形状，也就引申出了后面的平衡二叉树。
    给定一个元素集合，可以构造不同的二叉排序树，当它同时是一个完全二叉树的时候，查找的时间复杂度为O(log(n))，近似于二分查找。
    当出现最极端的斜树时，其时间复杂度为O(n)，等同于顺序查找，效果最差。
"""
class BSTNode:
    """
    定义一个二叉树节点类。
    以讨论算法为主，忽略了一些诸如对数据类型进行判断的问题。
    """
    def __init__(self, data, left=None, right=None):
        """
        初始化
        :param data: 节点储存的数据
        :param left: 节点左子树
        :param right: 节点右子树
        """
        self.data = data
        self.left = left
        self.right = right

class BinarySortTree:
    """
    基于BSTNode类的二叉排序树。维护一个根节点的指针。
    """
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        """
        关键码检索
        :param key: 关键码
        :return: 查询节点或None
        """
        bst = self._root
        while bst:
            entry = bst.data
            if entry > key:
                bst = bst.left
            elif entry < key:
                bst = bst.right
            else:
                print "Find", entry, "in BSTree!"

        print "can't find key", key, "!"

    def insert(self, key):
        """
        插入操作
        :param key:关键码
        :return: 布尔值
        """
        bst = self._root
        if not bst:
            self._root = BSTNode(key)
            return
        while True:
            entry = bst.data
            if key < entry:
                if bst.left is None:
                    bst.left = BSTNode(key)
                    return
                bst = bst.left
            elif key > entry:
                if bst.right is None:
                    bst.right = BSTNode(key)
                    return
                bst = bst.right
            else:
                bst.data = key
                return

    def delete(self, key):
        """
        二叉排序树最复杂的方法
        :param key: 关键码
        :return: 布尔值
        """
        p, q = None, self._root
        # 维持p为q的父节点，用于后面的链接操作
        if not q:
            print "Tree empty!"
            return
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:
                # 当树中没有关键码key时，结束退出。
                return

        # 上面已找到了要删除的节点，用q引用。而p则是q的父节点，或者None（q为根节点时）。
        if not q.left:
            if p is None:
                self._root = q.right
            elif q is p.left:
                p.left = q.right
            else:
                p.right = q.right
            return
        # 查找节点q的左子树的最右节点，将q的右子树链接为该节点的右子树
        # 该方法可能会增大树的深度，效率并不算高。可以设计其它的方法。
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right
        if p is None:
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def __iter__(self):
        """
        实现二叉树的 中序遍历 算法,
        展示我们创建的二叉排序树.
        直接使用python内置的列表作为一个栈。
        :return: data
        """
        stack = []
        node = self._root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            yield node.data
            node = node.right

    def preorder_digui(self, _root):
        """
        二叉树的前序遍历递归实现
        :param _root: root node
        :return: list
        """
        if _root == None:
            return []

        rt = [_root.data]
        left = self.preorder_digui(_root.left)
        right = self.preorder_digui(_root.right)
        return rt+left+right

    def preorder_stack(self):
        """
        二叉树的前序遍历非递归实现
        :return: list
        """
        if self._root == None:
            return None

        nodes = []
        nodes.append(self._root)
        elems = []

        while nodes:
            node = nodes.pop()
            elems.append(node.data)
            # 由于栈后进先出的原则
            if node.right:
                nodes.append(node.right)
            if node.left:
                nodes.append(node.left)

        return elems

    def inorder_digui(self, _root):
        """
        二叉树的中序遍历递归实现
        :param _root: root node
        :return: list
        """
        if _root == None:
            return []

        rt = [_root.data]
        left = self.inorder_digui(_root.left)
        right = self.inorder_digui(_root.right)
        return left+rt+right

    def inorder_stack(self):
        """
        二叉树的中序遍历非递归实现
            1. 使用一个栈保存结点（列表实现）；
            2. 如果结点存在，入栈，然后将当前指针指向左子树，直到为空；
            3. 当前结点不存在，则出栈栈顶元素，并把当前指针指向栈顶元素的右子树；
            4. 栈不为空，循环2、3。
        :return: list
        """
        if not self._root:
            return None

        nodes = []
        elems = []
        node = self._root
        while node or nodes:
            while node:
                nodes.append(node)
                node = node.left
            node = nodes.pop()
            elems.append(node.data)
            node = node.right

        return elems

    def postorder_digui(self, _root):
        """
        二叉树的后序遍历递归实现
        :param _root: root node
        :return: list
        """
        if _root == None:
            return []

        rt = [_root.data]
        left = self.postorder_digui(_root.left)
        right = self.postorder_digui(_root.right)
        return left+right+rt

    def postorder_stack(self):
        """
        二叉树的后序遍历非递归实现
            1.使用栈存储结点；
            2.当结点存在或者栈不为空，判断结点；
            3.当结点存在，结点值保存，结点入栈，并将指针指向结点的右子树；
            4.当栈不为空，结点出栈，并将指针指向左子树；
            5.重复2-4直到结果产生；
            6.逆序输出结果，利用Python列表的-1.
        :return:
        """
        if not self._root:
            return None

        elems = []
        nodes = []
        node = self._root

        while node or nodes:
            while node:
                elems.append(node.data)
                nodes.append(node)
                node = node.right
            if nodes:
                tmp = nodes.pop()
                node = tmp.left

        return elems[::-1]

    def traverse(self):
        """
        二叉树的层序遍历
        :return:
        """
        if self._root == None:
            return None

        nodes = [self._root]
        elems = [self._root.data]
        while nodes != []:
            tmp = nodes.pop(0)
            if tmp.left != None:
                nodes.append(tmp.left)
                elems.append(tmp.left.data)

            if tmp.right != None:
                nodes.append(tmp.right)
                elems.append(tmp.right.data)

        return elems

if __name__ == '__main__':
    lis = [62, 58, 88, 48, 73, 99, 35, 51, 93, 29, 37, 49, 56, 36, 50]
    bs_tree = BinarySortTree()
    for i in range(len(lis)):
        bs_tree.insert(lis[i])

    # 打印构造的二叉排序树
    lists = []
    for i in bs_tree:
        lists.append(i)
    print "BSTree is : ", lists
    # bs_tree.insert(100)
    # bs_tree.delete(58)
    bs_tree.search(5)

    pre = bs_tree.preorder_digui(bs_tree._root)
    print "递归前序遍历: ", pre
    pre2 = bs_tree.preorder_stack()
    print "非递归前序遍历: ", pre2

    ino = bs_tree.inorder_digui(bs_tree._root)
    print "递归中序遍历: ", ino
    ino2 = bs_tree.inorder_stack()
    print "非递归中序遍历: ", ino2

    pos = bs_tree.postorder_digui(bs_tree._root)
    print "递归后序遍历: ", pos
    pos2 = bs_tree.postorder_stack()
    print "非递归后序遍历: ", pos2

    level = bs_tree.traverse()
    print "层序遍历: ", level