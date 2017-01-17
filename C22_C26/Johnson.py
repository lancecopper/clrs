#func construct_matrix_pi_from_matrix_d failed
#我是按照这样的思路来的，如果i,j存在最短路径，
#且j的parent为i,需要满足条件：d[i][j] == d[i][k] + w[k][j]，
#但是满足这种条件的往往有多个k值，其中有的是因为j->k->j形成了0值环路，
#这不是一条简单路径，还有的是确实有多条i-->j的简单路径，
#在多条路径存在的情况下，最好的排除办法就是比对多条路径，
#哪条含边少哪条就是最短简单路径。然而我没有想到检查路径边数的实现。

from graph import Edge, DirectedGraph, NameVertex
from bellman_ford import bellman_ford
from dijkstra import dijkstra
from mst_kruskal import weight

def johnson(g, w):
    vertexes_g = g.get_v()
    edges_g = g.get_e()
    s = NameVertex('s')
    vertexes_g1 = [s] + vertexes_g
    edges_g1 = edges_g.copy()
    for vertex in vertexes_g:
        edges_g1.append(Edge(s, vertex, 0))
    graph2 = DirectedGraph(vertexes_g1, edges_g1)
    if bellman_ford(graph2, w, s) == False:
        print("the in put graph contains a negative_weight cycle")
    else:
        h = dict()
        for vertex in vertexes_g1:
            h[vertex] = vertex.d
        def weight1(edge):
            return w(edge) + h[edge.u] - h[edge.v]
    n = len(vertexes_g)
    d = dict()
    for u in vertexes_g:
        dijkstra(g, weight1, u)
        d[u] = dict()
        for v in vertexes_g:
            d[u][v] = v.d + h[v] - h[u]
    return d

def print_all_pairs_shortest_path(pi, i, j):
    i_name = getattr(vertexes[i - 1], 'name')
    j_name = getattr(vertexes[j - 1], 'name')
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
            u = vertexes[i - 1]
            v = vertexes[j - 1]
            uv_edge = g.find_edge(u, v)
            if i == j:
                w[i][j] = 0
            elif uv_edge is not None:
                w[i][j] = uv_edge.length
            else:
                w[i][j] = float("inf")
    return w

def construct_matrix_pi_from_matrix_d(d, w):
    n = len(d)
    matrix_pi = []
    for i in range(n):
        matrix_pi.append([None] * n)
    for i in range(1, n):
        for j in range(1, n):
            for k in range(1, n):
                if d[i][j] == d[i][k] + w[k][j] and \
                    i != k and i != j and j != k: #and \
                    #w[k][j] + d[j][k] != 0:
                    if not matrix_pi[i][j]: 
                        matrix_pi[i][j] = k
                        if w[k][j] + d[j][k] == 0:
                            print(i, j, k)
                            print(w[k][j], d[j][k])
                    #print(i,j,k)
                    #print(d[i][j], d[i][k], w[k][j])
            print('aha\n')
            #for num in matrix_pi:
            #    print(num)
    for i in range(1, n):
        for j in range(1, n):
            if i != j and w[i][j] < float("inf") and w[i][j] == d[i][j]:
                matrix_pi[i][j] = i
    return matrix_pi

if __name__ == "__main__":
    vertexes = []
    for vetex_name in '12345':
        vertexes.append(NameVertex('v' + vetex_name))
    v = [None] + vertexes
    edges = [Edge(v[1], v[2], 3), Edge(v[1], v[3], 8), Edge(v[1], v[5], -4),
             Edge(v[2], v[4], 1), Edge(v[2], v[5], 7), Edge(v[3], v[2], 4), 
             Edge(v[4], v[1], 2), Edge(v[4], v[3], -5), Edge(v[5], v[4], 6)]
    graph1 = DirectedGraph(vertexes, edges)
    matrix_w = trans_graph_into_matrix(graph1)
    d = johnson(graph1, weight)
    '''
    for k,v in d.items():
        print(type(v))
        for k1,v1 in v.items():
            print(k1, v1)
    '''
    n = len(vertexes)
    matrix_d = []
    for i in range(n + 1):
        matrix_d.append([None] * (n + 1))
    for k,v in d.items():
        for k1, v1 in v.items():
            i = vertexes.index(k) + 1
            j = vertexes.index(k1) + 1
            matrix_d[i][j] = v1
    matrix_pi = construct_matrix_pi_from_matrix_d(matrix_d, matrix_w)
    for i in matrix_w:
        print(i)
    for i in matrix_d:
        print(i)
    for i in matrix_pi:
        print(i)


    '''
    for i in range(1, len(vertexes) + 1):
        for j in range(1, len(vertexes) + 1):
            print("path from {} to {}:".format('v' + str(i), 'v' + str(j)))
            print_all_pairs_shortest_path(matrix_pi[n - 1], i, j)
            print(";  with length {}\n".format(matrix_d[i][j]))    
    '''






