"""
    二叉树模型
"""

class Node:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Bitree:
    def __init__(self,root = None):
        self.root = root

    def preorder(self,n):
        """
            先序遍历二叉树,根 左 右
        """
        if n is None:
            return
        print(n.value, end = "-")
        self.preorder(n.left)
        self.preorder(n.right)

    def midorder(self,n):
        """
            中序遍历二叉树, 左 根 右
        """       
        if n is None:
            return
        self.midorder(n.left)
        print(n.value, end= "-")
        self.midorder(n.right)

    def lastorder(self,n):
        """
            后序遍历二叉树, 左  右 根
        """       
        if n is None:
            return
        self.lastorder(n.left)
        self.lastorder(n.right)
        print(n.value, end= "-")
    
    def levelorder(self,n):
        """
        层次遍历 
        """
        orderlist = []
        orderlist.append(n)
        while len(orderlist) > 0:
            node = orderlist.pop(0)
            print(node.value,end= "-")
            if node.left:
                orderlist.append(node.left)
            if node.right:
                orderlist.append(node.right)
        


if __name__ == "__main__":
    b = Node("B")
    f = Node("F")
    g = Node("G")
    d = Node("D", f, g)
    i = Node("I")
    h = Node("H")
    e = Node("E", h, i)
    c = Node("C", d, e)
    a = Node("A", b, c)

    bt = Bitree(a)
    bt.preorder(bt.root)
    print("\n")
    bt.midorder(bt.root)
    print("\n")
    bt.lastorder(bt.root)
    print("\n")
    bt.levelorder(bt.root)
