from graph import Edge, DirectedGraph, NameVertex

def print_all_pairs_shortest_path(pi, i, j):
    i_name = getattr(eval('v' + str(i)), 'name')
    j_name = getattr(eval('v' + str(j)), 'name')
    if i == j:
        print(i_name, end = ' ')
    elif pi[i][j] is None:
        print("no path from {} to {} exists".format(i_name, j_name))
    else:
        print_all_pairs_shortest_path(pi, i, pi[i][j])
        print(j_name, end = ' ')

def extend_shortest_paths(l, w):
    n = len(l) - 1
    l1 = []
    for i in range(n + 1):
        temp = [None] * (n + 1)
        l1.append(temp)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            l1[i][j] = l[i][j]
            for k in range(1, n + 1):
                if l1[i][j] > l[i][k] + w[k][j]:
                    l1[i][j] = l[i][k] + w[k][j]
                    matrix_pi[i][j] = k
    return l1
def slow_all_pairs_shortest_paths(w):
    n = len(w) - 1
    l = [None] * n
    l[1] = w
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix_w[i][j] < float("inf"):
                matrix_pi[i][j] = i
    for m in range(2, n):
        l[m] = extend_shortest_paths(l[m - 1], w)
        '''
        print("matrix", m)
        for i in l[m]:
            print(i)
        print()
        '''
    return l[n - 1]
def faster_all_pairs_shortest_paths(w):
    n = len(w) - 1
    l = [None] * (2 * n)
    l[1] = w
    # initial matrix_pi
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if matrix_w[i][j] < float("inf"):
                matrix_pi[i][j] = i
    # main algorithm
    m = 1
    while m < n - 1:
        l[2 * m] = extend_shortest_paths(l[m], l[m])
        m *= 2
    return l[m]
def trans_graph_into_matrix(g):
    vertexes = g.get_v()
    n = len(vertexes)
    w = []
    for i in range(n + 1):
        temp = []
        for j in range(n + 1):
            temp.append(None)
        w.append(temp)
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            u = eval('v' + str(i))
            v = eval('v' + str(j))
            uv_edge = g.find_edge(u, v)
            if i == j:
                w[i][j] = 0
            elif uv_edge is not None:
                w[i][j] = uv_edge.length
            else:
                w[i][j] = float("inf")
    return w


if __name__ == "__main__":
    vertexes = []
    for vetex_name in '12345':
        temp_locals = locals()
        vetex_name = 'v' + vetex_name
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(v1, v2, 3), Edge(v1, v3, 8), Edge(v1, v5, -4),
             Edge(v2, v4, 1), Edge(v2, v5, 7), Edge(v3, v2, 4), 
             Edge(v4, v1, 2), Edge(v4, v3, -5), Edge(v5, v4, 6)]
    graph1 = DirectedGraph(vertexes, edges)
    matrix_w = trans_graph_into_matrix(graph1)
    matrix_pi = []
    for i in range(len(vertexes) + 1):
        matrix_pi.append([None] * (len(vertexes) + 1))
    result = slow_all_pairs_shortest_paths(matrix_w)
# factually matrix_w is valid only in the case of "slow_all_pairs_shortest_paths"
    #result1 = faster_all_pairs_shortest_paths(matrix_w)
    for i in range(1, len(vertexes) + 1):
        for j in range(1, len(vertexes) + 1):
            print("path from {} to {}:".format('v' + str(i), 'v' + str(j)))
            print_all_pairs_shortest_path(matrix_pi, i, j)
            print(";  with length {}\n".format(result[i][j]))
    #print(result == result1)






