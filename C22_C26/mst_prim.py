from clrs.C18_C21.disjoint_set import make_set, find_set, union
from graph import Edge, UnDirectedGraph, NameVertex
from mst_kruskal import weight

def mst_prim(g, w, r):
    vertexes = g.get_v()
    edges = g.get_e()
    for vertex in vertexes:
        vertex.key = float("inf")
        vertex.p = None
    vertexes = vertexes.copy()
    r.key = 0
    while len(vertexes):
        u = extract_v_with_min_key(vertexes)
        for v in g.adj(u):
            uv_edge = g.find_edge(u, v)
            if v in vertexes and w(uv_edge) < v.key:
                v.p = u
                v.key = w(uv_edge)
    result = set()
    vertexes = g.get_v()
    vertexes.remove(r)
    for vertex in vertexes:
        result.add(g.find_edge(vertex, vertex.p))
    return result

def extract_v_with_min_key(vertexes):
    min_key = float("inf")
    min_vertex = None
    for vertex in vertexes:
        if vertex.key < min_key:
            min_vertex = vertex
            min_key = vertex.key
    vertexes.remove(min_vertex)
    return min_vertex

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

    mst_edges = mst_prim(graph1, weight, vertexes[0])
    total_length = 0
    for edge in mst_edges:
        total_length += edge.length
        print("edge:", edge.u.name, edge.v.name, edge.length)
    print(total_length)





