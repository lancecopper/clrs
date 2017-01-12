# this module haven't pass a test
the_t = 2

class BTreeNode():
    def __init__(self, n = None, keys = None, t = None, leaf = False):
        self.n = n
        self.t = t
        self.leaf = leaf
        if keys:
            self.keys = [None] + keys
        else:
            self.keys = [None]
        self.c = [None]

class BTree():
    def __init__(self, root = None):
        self.root = root
    def insert(self, k):
        b_tree_insert(self, k)
    def delete(self, k):
        b_tree_delete(self.root, k)
    def search(self, k):
        return b_tree_search(self.root, k)


def disk_write(x):
    print("disk write", x, "...")

def disk_read(x):
    print("disk read", x, "...")

def b_tree_search(x, k):
    i = 1
    while i <= x.n and k > x.keys[i]:
        i += 1
    if i <= x.n and k == x.keys[i]:
        return x, i
    elif x.leaf:
        return
    else: 
        disk_read(x.c[i])
        return b_tree_search(x.c[i], k)

def b_tree_create(t):
    x = BTreeNode()
    x.leaf = True
    x.n = 0
    disk_write(x)
    t.root = x

def b_tree_insert(t, k):
    r = t.root
    if r.n == 2 * the_t - 1:
        s = BTreeNode()
        t.root = s
        s.leaf = False
        s.n = 0
        s.c.append(None)
        s.c[1] = r
        b_tree_split_child(s, 1)
        b_tree_insert_nonfull(s, k)
    else:
        b_tree_insert_nonfull(r, k)

def b_tree_split_child(x,i):
    z = BTreeNode()
    y = x.c[i]
    z.leaf = y.leaf
    z.n = the_t - 1
    for j in range(1, the_t):
        z.keys.append(None)
        z.keys[j] = y.keys[j + the_t]
        del(y.keys[j + the_t])
    if not y.leaf:
        for j in range(1, the_t + 1):
            z.c.append(None)
            z.c[j] = y.c[j + the_t]
            del(y.c[j + the_t])
    y.n = the_t- 1
    j = x.n + 1
    x.c.append(None)
    while j >= i + 1:
        x.c[j + 1] = x.c[j]
        j -= 1
    x.c[i + 1] = z
    j = x.n
    x.keys.append(None)
    while j >= i:
        x.keys[j + 1] = x.keys[j]
        j -= 1
    x.keys[i] = y.keys[the_t]
    del(y.keys[the_t])
    x.n = x.n + 1
    disk_write(y)
    disk_write(z)
    disk_write(x)


def b_tree_insert_nonfull(x, k):
    i = x.n
    if x.leaf:
        x.keys.append(None)
        while i >= 1 and k < x.keys[i]:
            x.keys[i + 1] = x.keys[i]
            i -= 1
        x.keys[i + 1] = k
        x.n = x.n + 1
        disk_write(x)
    else:
        while i >= 1 and k < x.keys[i]:
            i -= 1
        i += 1
        disk_read(x.c[i])
        if x.c[i].n == 2 * the_t - 1:
            b_tree_split_child(x, i)
            if k > x.keys[i]:
                i += 1
        b_tree_insert_nonfull(x.c[i], k)


def b_tree_insert(t, k):
    r = t.root
    if r.n == 2 * the_t- 1:
        s = BTreeNode()
        t.root = s
        s.leaf = False
        s.n = 0
        s.c.append(r)
        b_tree_split_child(s, 1)
        b_tree_insert_nonfull(s, k)
    else:
        b_tree_insert_nonfull(r, k)


def b_tree_union_child(x, i):
    y = x.c[i]
    z = x.c[i + 1]
    x1 = BTreeNode()
    x1.leaf = y.leaf
    x1.n = 2 * the_t - 1
    for i in range(1, the_t):
        x1.keys.append(y.keys[i])
    x1.keys.append(x.keys[i])
    for i in range(1, the_t):
        x1.key.append(z.keys[i])
    if not y.leaf:
        for i in range(1, the_t + 1):
            x1.c.append(y.c[i])
        for i in range(1, the_t + 1):
            x1.c.append(z.c[i])
    x.c[i] = x1
    del(x.keys[i])
    del(x.c[i + 1])
    x.n -= 1

def b_tree_delete(x, k):
    print("deleting", k, "in ele with keys", x.keys)
    i = 1
    while i <= x.n and k > x.keys[i]:
        i += 1
    if i <= x.n and k == x.keys[i] and x.leaf:
        print("enter 1..")
        x.keys.remove(k)
        x.n -= 1
    elif i <= x.n and k == x.keys[i]:
        print("enter 2..")
        if x.c[i].n >= the_t:
            temp_k = x.c[i].keys[n]
            x.keys[i] = temp_k
            b_tree_delete(x.c[i], temp_k)
        elif x.keys[i + 1].n >= the_t:
            temp_k = x.c[i + 1].keys[1]
            x.keys[i] = temp_k
            b_tree_delete(x.c[i + 1], temp_k)
        else:
            y = x.c[i]
            z = x.c[i + 1]
            y.keys.append(x.keys[i])
            for i in range(1, the_t):
                y.keys.append(z.keys[i])
            if not y.leaf:
                for i in range(1, the_t + 1):
                    y.c.append(z.c[i])
            y.n = 2 * the_t - 1
            del(x.keys[i])
            x.c.remove(z)
            x.n -= 1
            b_tree_delete(y, k)

            '''
            b_tree_union_child(x, i)
            y = x.c[i]
            b_tree_delete(y, k)
            '''
    else:
        print("enter 3..")
        y = x.c[i]
        if y.n == the_t - 1:
            if x.c[i - 1] and x.c[i - 1].n >= the_t:
                print('enter 31..')
                z = x.c[i - 1]
                y.keys.insert(1, x.keys[i - 1])
                x.keys[i - 1] = z.keys[z.n]
                if not y.leaf:
                    y.c.insert(1, z.c[z.n + 1])
                y.n  += 1
                del(z.keys[z.n])
                if not y.leaf:
                    del(z.c[z.n + 1])
                z.n -= 1
            elif i <= x.n and x.c[i + 1].n >= the_t:
                print('enter 32..')
                z = x.c[i + 1]
                #print("i, x.keys", i, x.keys)
                y.keys.append(x.keys[i])
                #print("###", z.keys)
                x.keys[i] = z.keys[1]
                #print("###", z.c)
                if not y.leaf:
                    y.c.append(z.c[1])
                y.n += 1
                del(z.keys[1])
                if not y.leaf:
                    del(z.c[1])
                z.n -= 1
            else:
                print('enter 33..')
                if x.c[i - 1]:
                    z = x.c[i - 1]
                elif len(x.c) > i + 1:
                    z = x.c[i + 1]
                else:
                    z = None
                if z:
                    y.keys.append(x.keys[i])
                    for i in range(1, the_t):
                        y.keys.append(z.keys[i])
                    if not y.leaf:
                        for i in range(1, the_t + 1):
                            y.c.append(z.c[i])
                    y.n = 2 * the_t - 1
                    del(x.keys[i])
                    x.c.remove(z)
                    x.n -= 1
                else:
                    x.leaf = True
                    x.c.remove(y)
        b_tree_delete(y, k)

def walk(t):
    print(t.keys)
    for x in t.c[1: len(t.c)]:
        walk(x)

if __name__ == "__main__":
    bt = BTree()
    b_tree_create(bt)
    for i in range(1, 6):
        print('insert', i)
        bt.insert(i)
    for i in range(1, 6):
        result = bt.search(i)
        print("find", i, "in the", result[1], "element", 
              "of node with keys :", result[0].keys, 
              "with n :", result[0].n)
    print("walking :")
    walk(bt.root)
    for i in range(1, 6):
        print("deleting :", i)
        bt.delete(i)
    r = bt.root
