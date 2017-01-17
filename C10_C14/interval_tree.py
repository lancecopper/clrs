import random
import red_black_tree, binary_tree
from red_black_tree import RBTreeNode, RBTree, rb_insert_fixup, \
    rb_delete_fixup, rb_transplant, tree_minimum, tree_minimum, \
    tree_maximum, tree_successor, tree_predecessor, tree_height

class Interval():
    def __init__(self, low, high):
        self.low = low
        self.high = high

class Interval_RBTreeNode(RBTreeNode):
    def __init__(self, interval = None, color = "None", 
                 left = None, right = None, p = None):
        self.interval = interval
        if self.interval:
            key = self.interval.low
        else:
            key = None
        self.max = -float('inf')
        super(Interval_RBTreeNode, self).__init__(key, color, left, 
                                                right, p)

nil = Interval_RBTreeNode(None,"black")
red_black_tree.nil = nil
binary_tree.nil = nil


class Interval_RBTree(RBTree):
    def __init__(self, root = None):
        super(Interval_RBTree, self).__init__(root)

    def insert(self, x):
        interval_insert(self, x)

    def delete(self, x):
        interval_delete(self, x)

    def search(self, i):
        return interval_search(self, i)


def interval_insert(t, z):
    print("insert key =", z.key)
    z.max = z.interval.high
    y = t.nil
    x = t.root
    while x is not t.nil:
        x.max = max(x.max, z.max)
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
    y.max = x.max
    x.max = max(x.interval.high, x.left.max, x.right.max)

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
    y.max = x.max
    x.max = max(x.interval.high, x.left.max, x.right.max)


def interval_delete(t, z):
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
        y.color = z.color
    while yp is not nil:
        print("yp is: ",  yp)
        yp.max = max(yp.interval.high, yp.left.max, yp.right.max)
        yp = yp.p
    if y_original_color == "black":
        rb_delete_fixup(t, x)
    print("suceed deleting key=", z.key) 


def interval_search(t, i):
    x = t.root
    while x is not t.nil and not (lambda x, y : 
        x.low <= y.high and y.low <= x.high)(x.interval, i):
        if x.left is not t.nil and x.left.max >= i.low:
            x = x.left
        else:
            x = x.right
    return x

for name in dir(red_black_tree):
    if name in dir():
        setattr(red_black_tree, name, eval(name))

if __name__ == "__main__":
    #for i in range(100):
    bt = Interval_RBTree()
    nodes = []

    for i in range(100):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        intv = Interval(min(x, y), max(x, y))
        node = Interval_RBTreeNode(intv)
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

    for i in range(1, 10):
        x = random.randint(1, 100)
        y = random.randint(1, 100)
        print("searching interval: ( ", x, y, ")")
        intv = Interval(min(x, y), max(x, y))
        a = bt.search(intv)
        if a is nil:
            print("failed")
        else:
            a = a.interval
            print("succeed searching element with interval: ( ", a.low, a.high, " )")


    print("maximum", bt.maximum().key)
    print("minimum", bt.minimum().key)
    print("successor", bt.successor(nodes[5]))
    print("predecessor", bt.predecessor(nodes[5]))







