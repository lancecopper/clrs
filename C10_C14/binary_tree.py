import random

nil = None

def testnil():
    print(nil)

'''
from hash_table import Node


def tree_search(x, k):
    if x is None or k == x.key:
        return x
    if k < x.key:
        return tree_search(x.left, k)
    else:
        return tree_search(x.right, k)
'''
def inorder_tree_walk(x):
    if x is not nil:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)

def preorder_tree_walk(x):
    if x is not nil:
        print(x.key)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)

def postorder_tree_walk(x):
    if x is not nil:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.key)

def tree_search(x, k):
    while x is not nil and k != x.key:
        if k < x.key:
            x = x.left
        else:
            x = x.right
    return x

def tree_minimum(x):
    while x.left is not nil:
        x = x.left
    return x

def tree_maximum(x):
    while x.right is not nil:
        x = x.right
    return x


def tree_successor(x):
    if x.right is not nil:
        return tree_minimum(x.right)
    y = x.p
    while y is not nil and x is y.right:
        x = y
        y = y.p
    return y

def tree_predecessor(x): 
    if x.left is not nil:
        return tree_maximum(x.left)
    y = x.p
    while y is not nil and x is y.left:
        x = y
        y = y.p
    return y

def tree_insert(t, z):
    y = nil
    x = t.root
    while x is not nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is nil:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z

def transplant(t, u, v):
    if u.p is nil:
        t.root = v
    elif u is u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not nil:
        v.p = u.p


def tree_delete(t, z):
    if z.left is nil:
        transplant(t, z, z.right)
    elif z.right is nil:
        transplant(t, z, z.left)
    else:
        y = tree_minimum(z.right)
        if y.p != z:
            transplant(t, y, y.right)
            y.right = z.right
            y.right.p = y
        transplant(t, z, y)
        y.left = z.left
        y.left.p = y    

def tree_height(z):
    if z is nil:
        return 0
    else:
        return 1 + max(tree_height(z.left), tree_height(z.right))


class BinaryTreeNode():
    def __init__(self, key, left = None, right = None, p = None):
        self.key = key
        self.left = left
        self.right = right
        self.p = p



class BinaryTree():
    def __init__(self, root = None):
        self.root = root

    def insert(self, z):
        tree_insert(self, z)

    def delete(self, z):
        tree_delete(self, z)

    def maximum(self):
        return tree_maximum(self.root)

    def minimum(self):
        return tree_minimum(self.root)

    def search(self, k):
        return tree_search(self.root, k)

    def successor(self, x):
        return tree_successor(x)

    def predecessor(self, x):
        return tree_predecessor(x)

    def inorder_tree_walk(self):
        inorder_tree_walk(self.root)

    def preorder_tree_walk(self):
        preorder_tree_walk(self.root)

    def postorder_tree_walk(self):
        postorder_tree_walk(self.root)

    def height(self):
        return tree_height(self.root)


if __name__ == "__main__":
    bt = BinaryTree()
    nodes = []
    for i in range(10):
        x = random.randint(1, 100)
        node = BinaryTreeNode(x)
        nodes.append(node)
        bt.insert(node)
    
    print(bt.root.key)

    print("inorder tree walk: ")
    bt.inorder_tree_walk()
    print("preorder tree walk: ")
    bt.preorder_tree_walk()
    print("postorder tree walk: ")
    bt.postorder_tree_walk()

    for i in range(5):
        bt.delete(nodes[i])

    print("inorder tree walk: ")
    bt.inorder_tree_walk()
    print("preorder tree walk: ")
    bt.preorder_tree_walk()
    print("postorder tree walk: ")
    bt.postorder_tree_walk()

    print("maximum", bt.maximum().key)
    print("minimum", bt.minimum().key)
    print("successor", bt.successor(nodes[5]))
    print("predecessor", bt.predecessor(nodes[5]))
    for i in range(1, 101):
        a = bt.search(i)
        if a:
            print(i, a)









