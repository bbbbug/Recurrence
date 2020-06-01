"""
    BFS问题：
        英文缩写为BFS即Breadth FirstSearch。其过程简单来说是对每一层节点依次访问，访问完一层进入下一层，
        而且每个节点只能访问一次，类似于数的层序遍历。
    非递归算法
"""
import queue


def BFS(nodes, node, visited):
    q = queue.Queue()
    if node is None:
        return
    visited.append(node)
    q.put(node)
    while not q.empty():
        qitem = q.get()
        for neighbor in nodes[qitem]:
            if neighbor not in visited:
                visited.append(neighbor)
                q.put(neighbor)
    return visited


"""
    DFS问题：
        英文缩写为DFS即Depth First Search.其过程简要来说是对每一个可能的分支路径深入到不能再深入为止，
        而且每个节点只能访问一次。
    递归三步曲：
        1.找终止条件， 结点无邻接点
        2.找返回值，
        3.本级递归应该做什么，判断该结点是否被遍历，若不是，找该结点的所有邻接点，迭代所有邻结点递归下去。
    递归过程：

"""


def DFS(nodes, node, visited):
    """
    深度遍历递归算法
    :param nodes: 待遍历的图
    :param node: 遍历起始位置
    :param visted: 已遍历的节点
    :return:
    """
    if node is None:
        return
    visited.append(node)
    for neighbor in nodes[node]:
        if neighbor not in visited:
            DFS(nodes, neighbor, visited)
    return visited


if __name__ == '__main__':
    graphs = {'a': ["b", "c"], 'b': ["c", "d"], 'c': ["e", "f"], 'd': 'f', 'e': '', 'f': ''}
    for node in list(graphs.keys()):
        visited = []
        print(BFS(graphs, node, visited))
