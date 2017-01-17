from graph import Edge, DirectedGraph, NameVertex
from mst_kruskal import weight
from bellman_ford import bellman_ford


class DifferenceConstraints():
    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b
        if a:
            self.m = len(a)
            self.n = len(a[0])
        else:
            self.m = None
            self.n = None

def trans_dc_to_graph_and_calc(dc):
    vertexes = []
    temp_locals = locals()
    for i in range(dc.n + 1):
        vetex_name = 'v' + str(i)
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = []
    for num in range(dc.m):
        i = a[num].index(-1) + 1
        j = a[num].index(1) + 1
        edge = Edge(eval('v' + str(i)), eval('v' + str(j)), b[num])
        edges.append(edge)
    for num in range(1, dc.n + 1):
        edge = Edge(eval('v0'), eval('v' + str(num)), 0)
        edges.append(edge)
    graph1 = DirectedGraph(vertexes, edges)
    bf_result = bellman_ford(graph1, weight, eval('v0'))
    result = None
    if bf_result:
        result = []
        for i in range(1, dc1.n + 1):
            result.append(getattr(eval('v' + str(i)), 'd'))
    return result


if __name__ == "__main__":
    a = [[1, -1, 0, 0, 0],
         [1, 0, 0, 0, -1],
         [0, 1, 0, 0, -1],
         [-1, 0, 1, 0, 0],
         [-1, 0, 1, 0, 0],
         [0, 0, -1, 1, 0],
         [0, 0, -1, 0, 1],
         [0, 0, 0, -1, 1]]
    b = [0, -1, 1, 5, 4, -1, -3, -3]
    dc1 = DifferenceConstraints(a, b)
    result = trans_dc_to_graph_and_calc(dc1)
    print(result)


    '''
    vertexes = []
    for i in range(dc1.n + 1):
        temp_locals = locals()
        vetex_name = 'v' + str(i)
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = []
    for num in range(dc1.m):
        i = a[num].index(-1) + 1
        j = a[num].index(1) + 1
        edge = Edge(eval('v' + str(i)), eval('v' + str(j)), b[num])
        edges.append(edge)
    for num in range(1, dc1.n + 1):
        edge = Edge(v0, eval('v' + str(num)), 0)
        edges.append(edge)
    graph1 = DirectedGraph(vertexes, edges)
    result = bellman_ford(graph1, weight, v0)
    if result:
        for i in range(1, dc1.n + 1):
            print('x{}:{}'.format(i, getattr(eval('v' + str(i)), 'd')), end = ',  ')
    print()

    '''

    