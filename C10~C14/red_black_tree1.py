import random
from binary_tree import BinaryTree, BinaryTreeNode

def inorder_tree_walk(x):
    if x is not nil:
        print(x.key, x.color)
        inorder_tree_walk(x.left)
        inorder_tree_walk(x.right)        

def preorder_tree_walk(x):
    if x is not nil:
        print(x.key, x.color)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)

def postorder_tree_walk(x):
    if x is not nil:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.key, x.color)

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
 

def tree_height(z):
    if z is nil:
        return 0
    else:
        return 1 + max(tree_height(z.left), tree_height(z.right))


def left_rotate(t, x):
    y = x.right
    x.right = y.left
    if y.left is not t.nil:
        y.left.p = x
    y.p = x.p
    if x.p is t.nil:
        t.root = y
    elif x is x.p.left:
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
    print("insert key =", z.key)
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
    z.left = t.nil
    z.right = t.nil
    z.color = "red"
    rb_insert_fixup(t, z)

def rb_insert_fixup(t, z):
    #print("rb_insert_fixup, key=", z.key)
    while z.p.color == "red":
        #print("z.p.color is red")
        if z.p is z.p.p.left:
            #print("z.p is z.p.p.left")
            y = z.p.p.right
            if y.color == "red":
                #print(1)
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z is z.p.right:
                #print(2)
                z = z.p
                left_rotate(t, z)
            else:
                z.p.color = "black"
                '''
                print("z.p, z.p.key:", z.p, z.p.key)
                print(t.root)
                print("z.p is nil:", z.p is t.nil)
                print("z is root", z is t.root)
                '''
                z.p.p.color = "red"
                right_rotate(t, z.p.p)
        else:
            #print("z.p is z.p.p.right")
            y = z.p.p.left
            if y.color == "red":
                #print(1)
                z.p.color = "black"
                y.color = "black"
                z.p.p.color = "red"
                z = z.p.p
            elif z is z.p.left:
                #print(2)
                z = z.p
                right_rotate(t, z)
            else:
                z.p.color = "black"
                '''
                print("z.p, z.p.key:", z.p, z.p.key)
                print(t.root)
                print("z.p is nil:", z.p is t.nil)
                print("z is root", z is t.root)
                '''
                z.p.p.color = "red"
                left_rotate(t, z.p.p)

    t.root.color = "black"

def rb_transplant(t, u, v):
    #print(u is nil)
    #print(u, u.key)
    if u.p is t.nil:
        t.root = v
    elif u is u.p.left:
        u.p.left = v
    else: 
        u.p.right = v
    v.p = u.p

def rb_delete(t, z):
    print("ready to delete key = ", z.key)
    y = z
    y_original_color = y.color
    if z.left is t.nil:
        x = z.right
        rb_transplant(t, z, z.right)
    elif z.right is t.nil:
        x = z.left
        rb_transplant(t, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        x = y.right
        if y.p is z:
            x.p = y
        else:
            rb_transplant(t, y, y.right)
            y.right = z.right
            y.right.p = y
        rb_transplant(t, z, y)
        y.left = z.left
        y.left.p = y
        y.color = z.color
    if y_original_color == "black":
        rb_delete_fixup(t, x)
    print("suceed deleting key=", z.key) 

def rb_delete_fixup(t, x):
    while x is not t.root and x.color == "black":
        if x is x.p.left:
            w = x.p.right
            if w.color == "red":
                print("enter case1")
                w.color = "black"
                x.p.color = "red"
                left_rotate(t, x.p)
                w = x.p.right
            if w.left.color == "black" and w.right.color == "black":
                print("enter case2")
                w.color = "red"
                x = x.p
            elif w.right.color == "black":
                print("enter case3")
                w.left.color = "black"
                w.color = "red"
                right_rotate(t, w)
                w = x.p.right
            else:
                print("enter case4")
                w.color = x.p.color
                x.p.color = "black"
                w.right.color = "black"
                left_rotate(t, x.p)
                x = t.root
        else:
            w = x.p.left
            if w.color == "red":
                print("enter case1")
                w.color = "black"
                x.p.color = "red"
                right_rotate(t, x.p)
                w = x.p.left
            if w.left.color == "black" and w.right.color == "black":
                print("enter case2")
                w.color = "red"
                x = x.p
            elif w.left.color == "black":
                print("enter case3")
                w.right.color = "black"
                w.color = "red"
                left_rotate(t, w)
                w = x.p.left
            else:
                print("enter case4")
                w.color = w.p.color
                w.p.color = "black"
                w.left.color = "black"
                right_rotate(t, x.p)
                x = t.root
    x.color = "black"



class RBTreeNode(BinaryTreeNode):
    def __init__(self, key = None, color = "None", left = None, 
                 right = None, p = None):
        self.color = color
        super(RBTreeNode, self).__init__(key, left, right, p)


nil = RBTreeNode(None,"black")

class RBTree(BinaryTree):
    def __init__(self, root = None):
        self.nil = nil
        if root:
            self.root = root
        else:
            self.root = self.nil

    def insert(self, x):
        rb_insert(self, x)

    def delete(self, x):
        rb_delete(self, x)


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
    #for i in range(1000):
    bt = RBTree()
    nodes = []

    for i in range(100):
        x = random.randint(1, 100)
        node = RBTreeNode(x)
        nodes.append(node)
        bt.insert(node)
        '''
        print("#############walk:")
        bt.preorder_tree_walk()
        print("#############over!")
        '''

    '''
    print("height:", bt.height())
    print(bt.root.key)

    print("inorder tree walk: ")
    bt.inorder_tree_walk()
    print("preorder tree walk: ")
    bt.preorder_tree_walk()
    print("postorder tree walk: ")
    bt.postorder_tree_walk()
    '''

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
        
    
