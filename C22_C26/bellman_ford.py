from graph import Edge, DirectedGraph, NameVertex
from mst_kruskal import weight
from bfs import print_path

def initialize_single_source(g, s):
    vertexes = g.get_v()
    for vertex in vertexes:
        vertex.d = float("inf")
        vertex.p = None
    s.d = 0
def relax(u, v, w, g):
    uv_edge = g.find_edge(u, v)
    if v.d > u.d + w(uv_edge):
        v.d = u.d + w(uv_edge)
        v.p = u
def bellman_ford(g, w, s):
    initialize_single_source(g, s)
    vertexes = g.get_v()
    edges = g.get_e()
    for i in range(len(vertexes) - 1):
        for edge in edges:
            relax(edge.u, edge.v, w, g)
    for edge in edges:
        if edge.v.d > edge.u.d + w(g.find_edge(edge.u, edge.v)):
            return False
    return True


if __name__ == "__main__":
    vertexes = []
    for vetex_name in 'stxyz':
        temp_locals = locals()
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(s, t, 6), Edge(s, y, 7), Edge(t, x, 5),
             Edge(t, y, 8), Edge(t, z, -4), Edge(x, t, -2), 
             Edge(y, x, -3), Edge(y, x, 9), Edge(z, s, 2), 
             Edge(z, x, 7)]
    graph1 = DirectedGraph(vertexes, edges)
    result = bellman_ford(graph1, weight, s)
    if result:
        for vertex in vertexes:
            print("path from vertex", s.name, "to vertex", vertex.name)
            print_path(graph1, s, vertex)
            print("\n")
            print("*******************\n")


