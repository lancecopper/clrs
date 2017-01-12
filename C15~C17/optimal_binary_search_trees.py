
def optimatl_bst(p, q, n):
    e = []
    w = []
    root = []
    for i in range(n + 2):
        temp1 = []
        temp2 = []
        for j in range(n + 1):
            temp1.append(None)
            temp2.append(None)
        e.append(temp1)
        w.append(temp2)
    for i in range(n + 1):
        temp = []
        for j in range(n + 1):
            temp.append(None)
        root.append(temp)
    for i in range(1, n + 2):
        e[i][i-1] = q[i-1]
        w[i][i-1] = q[i-1]
    for l in range(1, n + 1):
        for i in range(1, n - l + 2):
            j = i + l - 1
            e[i][j] = float("inf")
            w[i][j] = w[i][j - 1] + p[j] + q[j]
            for r in range(i, j + 1):
                t = e[i][r - 1] + e[r + 1][j] + w[i][j]
                #print(t, e[i][j], t<e[i][j])
                if t < e[i][j]:
                    e[i][j] = t
                    root[i][j] = r
    return e, root

def print_bst(root, p, i, j):
    if i > j:
        print("d[{}]".format(i), end = '')
    else:
        r = root[i][j]
        '''
        print("#####")
        print(r)
        print("#####")
        '''
        print(" tree(l:", end = '')
        print_bst(root, p, i, r - 1)
        print(", root:k[{}], r:".format(r), end = '')
        print_bst(root, p, r + 1, j)
        print(")", end = '')

if __name__ == "__main__":
    p = [None, 0.15, 0.10, 0.05, 0.10, 0.20]
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    e, root = optimatl_bst(p, q, 5)
    #print(e)
    #print(root)
    print_bst(root, p, 1, 5)
    print()


