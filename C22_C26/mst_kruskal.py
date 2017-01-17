from clrs.C18_C21.disjoint_set import make_set, find_set, union
from graph import Edge, UnDirectedGraph, NameVertex

def mst_kruskal(g, w):
    a = set()
    vertexes = g.get_v()
    edges = g.get_e()
    for vertex in vertexes:
        make_set(vertex)
    insertion_sort_weight(edges, w)
    for edge in edges:
        if find_set(edge.v) is not find_set(edge.u):
            a.add(edge)
            union(edge.u, edge.v)
    return a
def insertion_sort_weight(edges, w):
    length = len(edges)
    for i in range(1, length):
        key_edge = edges[i]
        key = w(edges[i])
        j = i - 1
        while j >= 0 and w(edges[j]) > key:
            edges[j + 1] = edges[j]
            j -= 1
        edges[j + 1] = key_edge

def weight(edge):
    return(edge.length)

if __name__ == "__main__":
    vertexes = []
    for vetex_name in 'abcdefghi':
        temp_locals = locals()
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(a, b, 4.0), Edge(a, h, 8.0), Edge(b, c, 8.0), 
             Edge(b, h, 11.0), Edge(c, d, 7.0), Edge(c, f, 4.0), 
             Edge(c, i, 2.0), Edge(d, e, 9.0), Edge(d, f, 14.0),
             Edge(e, f, 10.0), Edge(f, g, 2.0), Edge(g, h, 1.0), 
             Edge(g, i, 6.0), Edge(h, i, 7.0)]
    graph1 = UnDirectedGraph(vertexes, edges)

    
    # test for mst_kruskal
    mst_edges = mst_kruskal(graph1, weight)
    total_length = 0
    for edge in mst_edges:
        total_length += edge.length
        print("edge:", edge.u.name, edge.v.name, edge.length)
    print(total_length)







