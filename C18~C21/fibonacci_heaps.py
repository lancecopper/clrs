import random
import math

def max_degree(n):
    phi = (1 + pow(5, 0.5)) / 2
    return int(math.log(n, phi))

class Node():
    def __init__(self, key, p = None, children = [], 
                 degree = None, mark = False):
        self.key = key
        self.p = p
        self.children = children
        self.degree = degree
        self.mark = mark

class FibonacciHeaps():
    def __init__(self):
        self.min = None
        self.n = 0
        self.root_list = []
    def insert(self, x):
        fib_heap_insert(self, x)
    def delete(self, x):
        fib_heap_delete(self, x)
    def extract_min(self):
        return fib_heap_extract_min(self)
    def union(self, x):
        return fib_heap_union(self, x)
    def minimum(self):
        return fib_heap_minimum(self)

def make_fib_heap():
    return FibonacciHeaps()

def fib_heap_insert(h, x):
    x.degree = 0
    x.p = None
    x.children = []
    x.mark == False
    if h.min is None:
        h.root_list.append(x)
        h.min = x
    else:
        h.root_list.append(x)
        if x.key < h.min.key:
            h.min = x
    h.n += 1

def fib_heap_minimum(h):
    return h.min


def fib_heap_union(h1, h2):
    h = make_fib_heap()
    h.min = h1.min
    h.root_list = h1.root_list + h2.root_list
    if h1.min is None or \
       (h2.min is not None and h2.min.key < h1.min.key):
       h.min = h2.min
    h.n = h1.n + h2.n
    return h

def fib_heap_extract_min(h):
    z = h.min
    if z is not None:
        for child in z.children:
            h.root_list.append(child)
            child.p = None
        h.root_list.remove(z)
        if not len(h.root_list):
            h.min = None
        else:
            h.min = h.root_list[0]
            consolidate(h)
        h.n = h.n - 1
    return z

def fib_heap_link(h, y, x):
    #print("fib_heap_link x, y", x.key, y.key)
    h.root_list.remove(y)
    x.children.append(y)
    x.degree += 1
    y.mark = False

def consolidate(h):
    a = []
    for i in range(max_degree(h.n) + 1):
        a.append(None)
    temp_root_list = list(h.root_list)
    for w in temp_root_list:
        x = w
        d = x.degree
        while a[d] is not None:
            y = a[d]
            if x.key > y.key:
                x, y = y, x
            fib_heap_link(h, y, x)
            a[d] = None
            d += 1
        a[d] = x
    h.min = None
    for i in range(max_degree(h.n) + 1):
        if a[i] is not None:
            if h.min is None:
                h.root_list = [a[i]]
                h.min = a[i]
            else:
                h.root_list.append(a[i])
                if a[i].key < h.min.key:
                    h.min = a[i]


def fib_heap_decrease_key(h, x, k):
    if k > x.key:
        raise ValueError("new key is greater than current key")
    x.key = k
    y = x.p
    if y is not None and x.key < y.key:
        cut(h, x, y)
        cascading_cut(h, y)
    if x.key < h.min.key:
        h.min = x

def cut(h, x, y):
    y.children.remove(x)
    y.degree -= 1
    h.root_list.append(x)
    x.p = None
    x.mark = False

def cascadeing_cut(h, y):
    z = y.p
    if z is not None:
        if y.mark == False:
            y.mark = True
        else:
            cut(h, y, z)
            cascadeing_cut(h, z)

def fib_heap_delete(h, x):
    fib_heap_decrease_key(h, x, -float("inf"))
    fib_heap_extract_min(h)

if __name__ == "__main__":
    keys1 = []
    nodes1 = []
    fb1 = make_fib_heap()
    for i in range(100):
        node = Node(i)
        nodes1.append(node)
        keys1.append(i)
        fb1.insert(node)

    print(fb1.n)
    for node in fb1.root_list:
        print(node.key)
    '''
    for i in range(10):
        temp = fb1.extract_min()
        if temp:
            print("extract_min, ele with key: ", temp.key)
    '''
    for node in nodes1:
        print("minimum", fb1.minimum().key)
        fb1.delete(node)



    '''
    keys2 = []
    nodes2 = []
    fb2 = make_fib_heap()
    for i in range(100):
        node = Node(i)
        nodes2.append(node)
        keys2.append(i)
        fb2.insert(node)

    fb3 = fib_heap_union(fb1, fb2)
    for i in range(200):
        temp = fib_heap_extract_min(fb3)
        if temp:
            print("extract_min, ele with key: ", temp.key)
    '''










