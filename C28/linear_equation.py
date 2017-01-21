def lup_solve(l, u, p, b):
    n = len(l)
    x = [None] * n
    y = [None] * n
    for i in range(n):
        y[i] = b[p[i]]
        for j in range(i):
            y[i] -= l[i][j] * y[j]
    while i >= 0:
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= u[i][j] * x[j]
        x[i] /= u[i][i]
        x[i] = round(x[i], 4)
        i -= 1
    return x

def lu_decomposition(a):
    n = len(a)
    l = []
    u = []
    for i in range(n):
        l.append([None] * n)
        u.append([None] * n)
    for i in range(n):
        for j in range(i):
            u[i][j] = 0
        for j in range(i + 1, n):
            l[i][j] = 0
        l[i][i] = 1
    for k in range(n):
        u[k][k] = a[k][k]
        for i in range(k + 1, n):
            l[i][k] = a[i][k] / u[k][k]
            u[k][i] = a[k][i]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                a[i][j] = a[i][j] - l[i][k] * u[k][j]
    return l, u

def lup_decomposition(a):
    n = len(a)
    l = []
    u = []
    for i in range(n):
        l.append([None] * n)
        u.append([None] * n)
    for i in range(n):
        for j in range(i):
            u[i][j] = 0
        for j in range(i + 1, n):
            l[i][j] = 0
        l[i][i] = 1
    p = [None] * n
    for i in range(i):
        p[i] = 0
    for k in range(n):
        pp = 0
        for i in range(k, n):
            if abs(a[i][k]) > pp:
                pp = abs(a[i][k])
                k1 = i
        if pp == 0:
            raise ValueError("singular matirx")
        p[k], p[k1] = p[k1], p[k]
        for i in range(n):
            a[k][i], a[k1][i] = a[k1][i], a[k][i]
        for i in range(k + 1, n):
            a[i][k] = a[i][k] / a[k][k]
            for j in range(k + 1, n):
                a[i][j] = a[i][j] - a[i][k] * a[k][j]
    for i in range(n):
        for j in range(n):
            a[i][j] = round(a[i][j], 4)
    for k in range(n):
        u[k][k] = a[k][k]
        for i in range(k + 1, n):
            u[k][i] = a[k][i]
            l[i][k] = a[i][k]
    return l, u



if __name__ == "__main__":
    l = [[1,0,0],[0.2,1,0],[0.6,0.5,1]]
    u = [[5,6,3],[0,0.8,-0.6],[0,0,2.5]]
    p = [[0,0,1],[1,0,0],[0,1,0]]
    p = [2, 0, 1]
    b = [3, 7, 8]
    
    #a = [[1,2,0],[3,4,4],[5,6,3]]
    a = [[2,3,1,5],[6,13,5,19],[2,19,10,23],[4,10,11,31]]
    result1 = [-1.4, 2.2, 0.6]
    result = lup_solve(l, u, p, b) 
    if result1 == result:
        print("lup_solve worked fine~~")
    else:
        print("Error! lup_solve is wrong!")
    

    l, u = lu_decomposition(a)
    l1 = [[1,0,0,0],[3,1,0,0],[1,4,1,0],[2,1,7,1]]
    u1 = [[2,3,1,5],[0,4,2,4],[0,0,1,2],[0,0,0,3]]
    if l == l1 and u == u1:
        print("lu_decomposition worked fine~~")
    else:
        print("Error! lu_decomposition is wrong")


    a = [[2,0,2,0.6],[3,3,4,-2],[5,5,4,2],[-1,-2,3.4,-1]]
    l1 = [[1,0,0,0],[0.4,1,0,0],[-0.2,0.5,1,0],[0.6,0,0.4,1]]
    u1 = [[5,5,4,2],[0,-2,0.4,-0.2],[0,0,4,-0.5],[0,0,0,-3]]
    l, u = lup_decomposition(a)
    print(l)
    print(u)
    if l == l1 and u == u1:
        print("lup_decomposition worked fine~~")
    else:
        print("Error! lup_decomposition is wrong")





