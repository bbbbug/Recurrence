"""
    树的遍历问题：
        树的遍历总共有四种，前序遍历、后序遍历、中序遍历、层次遍历

    递归三步曲：
        1.找终止条件，
        2.找返回值，
        3.本级递归应该做什么，

    递归过程：
"""


class Node:
    """节点类"""

    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree:
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def listCreatTree(self, root, nodes, i):
        """
        通过列表创建二叉树
        :param root: 根节点
        :param nodes: 节点值列表
        :param i: 从列表的index开始创建root
        :return:  返回二叉树
        """
        if i < len(nodes):
            if nodes[i] == 0:
                return None  # 这里的return很重要
            else:
                root = Node(nodes[i])
                # 往左递推
                root.lchild = self.listCreatTree(root.lchild, nodes, 2 * i + 1)  # 从根开始一直到最左，直至为空，
                # 往右回溯
                root.rchild = self.listCreatTree(root.rchild, nodes, 2 * i + 2)  # 再返回上一个根，回溯右，
        return root

    def preOrder(self, treeNode, results):
        """
        递归先序遍历二叉树
        :param treeNode: 遍历根节点
        :param results: 返回遍历后的列表
        :return:
        """
        if treeNode:
            if treeNode.elem != 0:
                results.append(treeNode.elem)
            if treeNode.lchild:
                self.preOrder(treeNode.lchild, results)
            if treeNode.rchild:
                self.preOrder(treeNode.rchild, results)
        return results

    def midOrder(self, treeNode, results):
        """
        递归中序遍历二叉树
        :param treeNode: 遍历根节点
        :param results: 返回遍历后的列表
        :return:
        """
        if treeNode:
            if treeNode.lchild:
                self.midOrder(treeNode.lchild, results)
            if treeNode.elem != 0:
                results.append(treeNode.elem)
            if treeNode.rchild:
                self.midOrder(treeNode.rchild, results)
        return results

    def posOrder(self, treeNode, results):
        """
        递归先序遍历二叉树
        :param treeNode: 遍历根节点
        :param results: 返回遍历后的列表
        :return:
        """
        if treeNode:
            if treeNode.lchild:
                self.posOrder(treeNode.lchild, results)
            if treeNode.rchild:
                self.posOrder(treeNode.rchild, results)
            if treeNode.elem != 0:
                results.append(treeNode.elem)
        return results


if __name__ == '__main__':
    t = Tree()
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 0, 0, 'h', 0, 0, 'i']
    tree = t.listCreatTree(None, nodes, 0)
    results = []
    print(t.midOrder(tree, results))

