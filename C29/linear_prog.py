import copy
def pivot(argn, argb, arga, b, c, v, l, e):
    '''
    print("pivot args:")
    print("argn:", argn)
    print("argb:", argb)
    print("arga:", arga)
    print("b", b)
    print("c", c)
    print("v", v)
    print("l", l)
    print("e", e)
    '''
    #Compute the coefficients of the equation for new basic variable xe.
    argn1 = argn.copy()
    argn1.append(l)
    argn1.remove(e)
    argn1.sort()
    argb1 = argb.copy()
    argb1.append(e)
    argb1.remove(l)
    argb1.sort()
    m = len(arga)
    n = len(arga[0])
    arga1 = []
    for i in range(m):
        arga1.append([0] * n)
    b1 = [0] * len(b)
    c1 = [0] * len(c)
    v1 = None
    b1[e] = b[l] / arga[l][e]
    temp_argn = argn.copy()
    temp_argn.remove(e)
    for j in temp_argn:
        arga1[e][j] = arga[l][j] / arga[l][e]
    arga1[e][l] = 1 / arga[l][e]
    #Compute the coefficients of the remaining constraints
    temp_argb = argb.copy()
    temp_argb.remove(l)
    for i in temp_argb:
        b1[i] = b[i] - arga[i][e] * b1[e]
        for j in temp_argn:
            arga1[i][j] = arga[i][j] - arga[i][e] * arga1[e][j]
        arga1[i][l] = - arga[i][e] * arga1[e][l]
    #Comupte the objective function
    v1 = v + c[e] * b1[e]
    for j in temp_argn:
        c1[j] = c[j] - c[e] * arga1[e][j]
    c1[l] = - c[e] * arga1[e][l]
    #Compute new sets of basic and nonbasic variables
    return argn1, argb1, arga1, b1, c1, v1

def simplex(arga, b, c):
    m = len(arga)
    n = len(arga[0])
    argn, argb, arga, b, c, v = initial_simplex(arga, b, c)
    delta = [float("inf")] * (m + n)
    calc_num = 0
    while calc_num <= m + n:
        print("simplex loop:")
        '''
        print("argn:", argn)
        print("argb:", argb)
        print("arga:", arga)
        print("b", b)
        print("c", c)
        print("v", v)
        print("calc_num", calc_num)
        '''
        calc_num += 1
        e = None
        for j in argn:
            if c[j] > 0:
                e = j
                break
        if e is None:
            break
        for i in argb:
            if arga[i][e] > 0:
                delta[i] = b[i] / arga[i][e]
            else:
                delta[i] = float("inf")
        min_delta = float("inf")
        min_l = None
        for l in argb:
            if delta[l] < min_delta:
                min_delta = delta[l]
                min_l = l
        l = min_l
        if min_delta == float("inf"):
            return "unbounded"
        else:
            argn, argb, arga, b, c, v = pivot(argn, argb, arga, b, c, v, l, e)
    x = [None] * (m + n)
    for i in range(m + n):
        if i in argb:
            x[i] = b[i]
        else:
            x[i] = 0
    print("ret from simplex!!!")
    return x, v

def initial_simplex(arga, b, c):
    ori_v = 0
    ori_c = c
    m = len(arga)
    n = len(arga[0])
    #test whether the basic solution is feasible
    min_bi = float("inf")
    k = None
    for i in range(len(b)):
        if b[i] < min_bi:
            min_bi = b[i]
            k = i
    if min_bi >= 0:
        for row in arga:
            row.extend([0] * m)
            c.append(0)
        for i in range(n):
            arga.insert(0, ([0] * (m + n)))
            b.insert(0, 0)
        return list(range(n)), list(range(n, n + m)), arga, b, c, ori_v
    c_aux = [0] * (m + n)
    c_aux.insert(0, -1)
    a_aux = copy.deepcopy(arga)
    for row in a_aux:
        row.insert(0, -1)
        row.extend([0] * m)
    n += 1
    for i in range(n):
        a_aux.insert(0, ([0] * (m + n)))
        b.insert(0, 0)
    l = k + n
    argn, argb, arga, b, c, v = pivot(list(range(n)), list(range(n, n + m)), \
        a_aux, b, c_aux, 0, l, 0)
    print("get from pivot:")
    print("argn:", argn)
    print("argb:", argb)
    print("arga:", arga)
    print("b", b)
    print("c", c)
    print("v", v)
    #while loop copied from simplex
    delta = [float("inf")] * (m + n)
    calc_num = 0
    while calc_num <= m + n:
        print("calc_num", calc_num)
        calc_num += 1
        e = None
        for j in argn:
            if c[j] > 0:
                e = j
                break
        if e is None:
            break
        for i in argb:
            if arga[i][e] > 0:
                delta[i] = b[i] / arga[i][e]
            else:
                delta[i] = float("inf")
        min_delta = float("inf")
        min_l = None
        for l in argb:
            if delta[l] < min_delta:
                min_delta = delta[l]
                min_l = l
        l = min_l
        #print("delta:",delta)
        #print("###min_delta, min_l", min_delta, min_l)
        #print("####l,e,argb,argn", l,e,argb,argn)
        if min_delta == float("inf"):
            return "unbounded"
        else:
            argn, argb, arga, b, c, v = pivot(argn, argb, arga, b, c, v, l, e)
    if v == 0:
        if 0 in argb:
            for e in argn:
                if arga[0][e] != 0:
                    break
            argn, argb, arga, b, c, v = pivot(argn, argb, arga, b, c, v, 0, e)
        argn.remove(0)
        del(b[0])
        del(arga[0])
        for row in arga:
            del(row[0])
        for i in range(len(argb)):
            argb[i] -= 1
        for i in range(len(argn)):
            argn[i] -= 1
        c = ori_c
        v = ori_v
        c.extend([0] * m)
        for i in argb:
            if c[i] != 0:
                v += c[i] * b[i]
                for j in argn:
                    c[j] -= c[i] * arga[i][j]
                c[i] = 0
        return argn, argb, arga, b, c, v
    else:
        return "infeasible"

if __name__ == "__main__":
    '''
    #print("@@@test for initial_simplex and pivot:")
    arga = [[2, -1], [1, -5]]
    b = [2, -4]
    c = [2, -1]
    argn, argb, arga, b, c, v = initial_simplex(arga, b, c)
    print("ret from initial simplex:")
    print("argn:", argn)
    print("argb:", argb)
    print("arga:", arga)
    print("b:", b)
    print("c", c)
    print("v", v)
    print("object function is:")
    print("z = {} ".format(v), end = "")
    for j in argn:
        if c[j]:
            print("+ {} * x{} ".format(c[j], j + 1), end = "")
    print()
    print("restrictions are:")
    for i in argb:
        print("x{} = {} ".format(i + 1, b[i]), end = "")
        for j in argn:
            if arga[i][j]:
                print("- {} * x{} ".format(arga[i][j], j + 1), end = "")
        print()
    '''
    print("@@@test for simplex:")
    arga = [[1, 1, 3], [2, 2, 5], [4, 1, 2]]
    b = [30, 24, 36]
    c = [3, 1, 2]
    x, v = simplex(arga, b, c)
    print(x, v)
    





