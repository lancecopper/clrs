from graph import Edge, DirectedGraph, NameVertex
from mst_kruskal import weight
from bfs import print_path
from topological_sort import topological_sort
from bellman_ford import initialize_single_source, relax


def dijkstra(g, w, s):
    initialize_single_source(g, s)
    s_result = []
    vertexes = g.get_v().copy()
    while len(vertexes):
        u = extract_u_with_min_d(vertexes)
        s_result.append(u)
        for v in g.adj(u):
            relax(u, v, w, g)
def extract_u_with_min_d(vertexes):
    min_key = float("inf")
    min_vertex = None
    for vertex in vertexes:
        if vertex.d < min_key:
            min_vertex = vertex
            min_key = vertex.d
    vertexes.remove(min_vertex)
    return min_vertex

if __name__ == "__main__":
    vertexes = []
    for vetex_name in 'stxyz':
        temp_locals = locals()
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(s, t, 10), Edge(s, y, 5), Edge(t, x, 1), 
             Edge(t, y, 2), Edge(x, z, 4), Edge(y, t, 3), 
             Edge(y, x, 9), Edge(y, z, 2), Edge(z, s, 7),
             Edge(z, x, 6)]
    graph1 = DirectedGraph(vertexes, edges)
    dijkstra(graph1, weight, s)
    for vertex in vertexes:
        print("path from vertex", s.name, "to vertex", vertex.name)
        print_path(graph1, s, vertex)
        print("\n")
        print("*******************\n")






