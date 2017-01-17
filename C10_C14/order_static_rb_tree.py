import random
import red_black_tree, binary_tree
from red_black_tree import RBTreeNode, RBTree, rb_insert_fixup, \
    rb_delete_fixup, rb_transplant, tree_minimum, tree_minimum, \
    tree_maximum, tree_successor, tree_predecessor, tree_height



class OSRBTreeNode(RBTreeNode):
    def __init__(self, key = None, color = "None", size = 0, left = None, 
                 right = None, p = None):
        self.size = size
        super(OSRBTreeNode, self).__init__(key, color, left, right, p)

class OSRBTree(RBTree):
    def __init__(self, root = None):
        super(OSRBTree, self).__init__(root)

    def select(self, i):
        return os_select(self.root, i)

    def rank(self, x):
        return os_rank(self, x)



nil = OSRBTreeNode(None,"black")
red_black_tree.nil = nil
binary_tree.nil = nil


def os_select(x, i):
    r = x.left.size + 1
    if i == r:
        return x
    elif i < r:
        return os_select(x.left, i)
    else:
        return os_select(x.right, i-r)

def os_rank(t, x):
    r = x.left.size + 1
    y = x
    while y is not t.root:
        if y is y.p.right:
            r = r + y.p.left.size + 1
        y = y.p
    return r

def rb_insert(t, z):
    #print("insert key =", z.key)
    y = t.nil
    x = t.root
    while x is not t.nil:
        x.size += 1
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
    z.size = 1
    z.left = t.nil
    z.right = t.nil
    z.color = "red"
    rb_insert_fixup(t, z)


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
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

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
    y.size = x.size
    x.size = x.left.size + x.right.size + 1

def rb_delete(t, z):
    print("ready to delete key = ", z.key)
    y = z
    y_original_color = y.color
    yp = y.p
    if z.left is t.nil:
        x = z.right
        rb_transplant(t, z, z.right)
    elif z.right is t.nil:
        x = z.left
        rb_transplant(t, z, z.left)
    else:
        y = tree_minimum(z.right)
        y_original_color = y.color
        yp = y.p
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
        y.size = y.left.size + y.right.size + 1
        y.color = z.color
    while yp is not nil:
        #print("yp is: ",  yp)
        yp.size -= 1
        yp = yp.p
    if y_original_color == "black":
        rb_delete_fixup(t, x)
    print("suceed deleting key=", z.key) 


for name in dir(red_black_tree):
    if name in dir():
        setattr(red_black_tree, name, eval(name))


if __name__ == "__main__":
    #for i in range(1000):
    bt = OSRBTree()
    nodes = []

    for i in range(100):
        x = random.randint(1, 100)
        node = OSRBTreeNode(x)
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
    nodes1 = list(nodes)
    for i in range(5):
        bt.delete(nodes[i])
        nodes1.remove(nodes[i])


    print("inorder tree walk: ")
    bt.inorder_tree_walk()
    '''
    print("preorder tree walk: ")
    bt.preorder_tree_walk()
    print("postorder tree walk: ")
    bt.postorder_tree_walk()
    '''
    test1 = []
    print("########## select:")
    for i in range(1, 96):
        x = bt.select(i)
        test1.append((i, x.key))
        print("the", i , "element's key is",  x.key)
    test1.sort()

    test2 = []
    print("########## rank:")
    for node in nodes1:
        r = bt.rank(node)
        test2.append((r, node.key))
        print("key = ", node.key, "element's rank is", r)
    test2.sort()

    print("rank and select worked well: ", test2 == test1)


'''
    print("maximum", bt.maximum().key)
    print("minimum", bt.minimum().key)
    print("successor", bt.successor(nodes[5]))
    print("predecessor", bt.predecessor(nodes[5]))
    for i in range(1, 101):
        a = bt.search(i)
        if a:
            print(i, a)
'''
