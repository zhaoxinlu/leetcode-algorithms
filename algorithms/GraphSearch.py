# -*- coding: utf-8 -*-
"""
Editor: Zhao Xinlu
School: BUPT
Date: 2018-01-25
Function: 图的数据结构与深度/广度优先搜索
"""
class Graph(object):
    def __init__(self, *args, **kwargs):
        self.neighbors_nodes = {}

    def nodes(self):
        return self.neighbors_nodes.keys()

    def add_node(self, node):
        if not node in self.nodes():
            self.neighbors_nodes[node] = []

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_edge(self, edge):
        u, v = edge # u -> v, v -> u
        if v not in self.neighbors_nodes[u] and u not in self.neighbors_nodes[v]:
            self.neighbors_nodes[u].append(v)
            if u != v:
                self.neighbors_nodes[v].append(u)

    def breadth_first_search(self, root=None):
        """
        广度优先搜索
        :param root:
        :return:
        """
        queue = []
        result = []
        visited = {}
        def BFS():
            while len(queue) > 0:
                node = queue.pop(0)

                visited[node] = True
                for nd in self.neighbors_nodes[node]:
                    if nd not in visited and nd not in queue:
                        queue.append(nd)
                        result.append(nd)

        if root:
            queue.append(root)
            result.append(root)
            BFS()

        for node in self.nodes():
            if node not in visited:
                queue.append(node)
                result.append(node)
                BFS()

        return result

    def depth_first_search(self, root=None):
        """
        深度优先搜索
        :param root:
        :return:
        """
        visited_ = {}
        result = []
        def DFS(node):
            visited_[node] = True
            result.append(node)
            for nd in self.neighbors_nodes[node]:
                if nd not in visited_:
                    DFS(nd)

        if root:
            DFS(root)

        for node in self.nodes():
            if node not in visited_:
                DFS(node)

        return result

if __name__ == '__main__':
    g = Graph()
    g.add_nodes([i+1 for i in range(8)])
    g.add_edge((1, 2))
    g.add_edge((1, 3))
    g.add_edge((2, 6))
    g.add_edge((2, 5))
    g.add_edge((4, 8))
    g.add_edge((5, 8))
    g.add_edge((3, 6))
    g.add_edge((3, 7))
    g.add_edge((6, 7))

    result1 = g.breadth_first_search(1)
    print "广度优先搜索：", result1

    result2 = g.depth_first_search(1)
    print "深度优先搜索：", result2