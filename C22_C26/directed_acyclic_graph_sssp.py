from graph import Edge, DirectedGraph, NameVertex
from mst_kruskal import weight
from bfs import print_path
from topological_sort import topological_sort
from bellman_ford import initialize_single_source, relax

def dag_shortest_paths(g, w, s):
    vertexes = topological_sort(g)
    initialize_single_source(g, s)
    edges = g.get_e()
    for u in vertexes:
        for v in g.adj(u):
            relax(u, v, w, g)
if __name__ == "__main__":
    vertexes = []
    for vetex_name in 'rstxyz':
        temp_locals = locals()
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(r, s, 5), Edge(r, t, 3), Edge(s, t, 2), 
             Edge(s, x, 6), Edge(t, x, 7), Edge(t, y, 4), 
             Edge(t, z, 2), Edge(x, y, -1), Edge(x, z, 1), 
             Edge(y, z, -2)]
    graph1 = DirectedGraph(vertexes, edges)
    dag_shortest_paths(graph1, weight, s)
    for vertex in vertexes:
        print("path from vertex", s.name, "to vertex", vertex.name)
        print_path(graph1, s, vertex)
        print("\n")
        print("*******************\n")



