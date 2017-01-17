#func construct_matrix_pi_from_matrix_d failed

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

def floyd_warshall(w):
    n = len(w)
    d = [None] * n
    d[0] = w
    for k in range(1, n):
        d[k] = []
        for i in range(n):
            d[k].append([None] * n)
        for i in range(1, n):
            for j in range(1, n):
                if d[k - 1][i][j] <= d[k - 1][i][k] + d[k - 1][k][j]:
                    d[k][i][j] = d[k - 1][i][j]
                    matrix_pi[k][i][j] = matrix_pi[k - 1][i][j]
                else:
                    d[k][i][j] = d[k - 1][i][k] + d[k - 1][k][j]
                    matrix_pi[k][i][j] = matrix_pi[k - 1][k][j]
    return d[n - 1]

def transitive_closure(g):
    vertexes = g.get_v()
    n = len(vertexes)
    t = [None] * (n + 1)
    for i in range(n + 1):
        t[i] = []
        for j in range(n + 1):
            t[i].append(([None] * (n + 1)))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j or g.find_edge(eval('v' + str(i)), eval('v' + str(j))):
                t[0][i][j] = 1
            else:
                t[0][i][j] = 0
    for i in t[0]:
        print(i)
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                t[k][i][j] = t[k - 1][i][j] or t[k - 1][i][k] and t[k - 1][k][j]
                print(t[k][i][j], t[k - 1][i][j], t[k - 1][i][k] and t[k - 1][k][j] )
                print(t[k - 1][i][k], t[k - 1][k][j])
                print('###')
    return t[n]

'''
def construct_matrix_pi_from_matrix_d(d, w):
    n = len(d)
    matrix_pi = []
    for i in range(n):
        matrix_pi.append([None] * n)
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if d[i][j] == d[i][k] + w[k][j] and \
                    i != k and i != j and not w[k][j] + d[j][k] != 0: 
                    matrix_pi[i][j] = k
                    print(i,j,k)
                    #print(d[i][j], d[i][k], w[k][j])
            print('aha\n')
            #for num in matrix_pi:
            #    print(num)
    return matrix_pi
'''

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
    n = len(matrix_w)
    matrix_pi = [None] * n
    for i in range(n):
        matrix_pi[i] = []
        for j in range(n):
            matrix_pi[i].append([None] * n)
    for i in range(1, n):
        for j in range(1, n):
            if i != j and matrix_w[i][j] < float("inf"):
                matrix_pi[0][i][j] = i
    matrix_d = floyd_warshall(matrix_w)
    for i in matrix_pi[n - 1]:
        print(i)
    for i in range(1, len(vertexes) + 1):
        for j in range(1, len(vertexes) + 1):
            print("path from {} to {}:".format('v' + str(i), 'v' + str(j)))
            print_all_pairs_shortest_path(matrix_pi[n - 1], i, j)
            print(";  with length {}\n".format(matrix_d[i][j]))

    vertexes2 = []
    t_closure = transitive_closure(graph2)
    print("t_closure...")
    for t_c in t_closure:
        print(t_c)



