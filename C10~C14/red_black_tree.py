from binary_tree import *

def left_rotate(t, x):
    y = x.right
    x.right = y.left:
    if y.left is not t.nil:
        y.left.p = x
    y.p = x.p
    if x.p is t.nil:
        t.root = y
    elif x if x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.left = x
    x.p = y

def right_rotate(t, x):
    y = x.left
    x.left = y.right
    if y.right is not t.nil:
        y.right.p = x
    y.p = x.p
    if x.p is t.nil:
        t.root = y
    elif x is x.p.left:
        x.p.left = y
    else:
        x.p.right = y
    y.right = x
    x.p = y

def rb_insert(t, z):
    y = t.nil
    x = t.root
    while x is not t.nil:
        y = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = y
    if y is t.nil:
        t.root = z
    elif z.key < y.key:
        y.left = z
    else:
        y.right = z
    z.left = T.nil
    z.right = T.nil
    z.color = "red"
    rb_insert_fixup(t, z)

def rb_insert_fixup(t, z):
    while z.p.color == "red":
        if z.p == z.p.p.left:
            y = z.p.p.right
            if y.color == "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z == z.p.right:
                z = z.p
                left_rotate(t, z)
            z.p.color = "black"
            z.p.p.color = "red"
            right_rotate(t, z.p.p)
        else:
            y = z.p.p.left
            if y.color == "red":
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z == z.p.left:
                z = z.p
                right_rotate(t, z)
            z.p.color = "black"
            z.p.p.color = "red"
            left_rotate(t, z.p.p)

    t.root.color = "black"

def rb_transplant(T, u, v)



class RBTreeNode(BinaryTreeNode):
    def __init__(self, color = None, key = None, left = None, 
                 right = None, p = None):
        self.color = color
        super(RBTreeNode, self).__init__(key, left, right, p)


class RBTree(BinaryTree):
    def __init__(self)
        self.nil = RBTreeNode("black")

    def insert(self, x):
        rb_insert(self, x)

    def delete(self, x):





if __name__ == "__main__":
    a = RBTreeNode("black", 1, 1, 1, 1)

