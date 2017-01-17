import random
from graph import Edge, DirectedGraph, NameVertex
from topological_sort import topological_sort
from dfs import dfs


def strongly_connected_components(g):
    vertexes = topological_sort(g)
    vertexes.reverse()
    print("first dfs")
    for i in vertexes:
        print(i.name, i.d, i.f)
    edges = g.get_e()
    t_edges = []
    for edge in edges:
        t_edge = Edge(edge.v, edge.u)
        t_edges.append(t_edge)
    t_g = transposed_g = DirectedGraph(vertexes, t_edges)
    dfs(t_g)
    vertexes = t_g.get_v()
    quick_sort_detect(vertexes, 0, len(vertexes) - 1)
    print("second dfs")
    for i in vertexes:
        print(i.name, i.d, i.f)
    return print_component(vertexes)

def print_component(vertexes):
    components = []
    max_final = vertexes[0].f
    print("new_component:")
    for i in range(len(vertexes)):
        component = []
        if vertexes[i].f <= max_final:
            component.append(vertexes[i])
            print(vertexes[i].name, end = ', ')
        else:
            components.append(component)
            component = []
            component.append(vertexes[i])
            max_final = vertexes[i].f
            print("\nnew_component:")
            print(vertexes[i].name, end = ', ')
    components.append(component)
    print()
    return components
def quick_sort_detect(vertexes, p, q):
    if p < q:
        r = partion(vertexes, p, q)
        quick_sort_detect(vertexes, p, r)
        quick_sort_detect(vertexes, r + 1, q)
def partion(vertexes, p, q):
    r = random.randint(p, q)
    vertexes[r], vertexes[q] = vertexes[q], vertexes[r]
    x = vertexes[q].d
    j = p - 1
    for i in range(p, q):
        if vertexes[i].d < x:
            j += 1
            vertexes[j], vertexes[i] = vertexes[i], vertexes[j]
    vertexes[j + 1], vertexes[q] = vertexes[q], vertexes[j + 1]
    return j + 1

if __name__ == "__main__":
    #vetex_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    vertexes = []
    for vetex_name in 'abcdefgh':
        temp_locals = locals()
        temp_locals[vetex_name] = NameVertex(vetex_name)
        vertexes.append(eval(vetex_name))
    edges = [Edge(a, b), Edge(b, c), Edge(b, e), Edge(b, f), Edge(c, d),
             Edge(c, g), Edge(d, c), Edge(d, h), Edge(e, a), Edge(e, f),
             Edge(f, g), Edge(g, f), Edge(g, f), Edge(h, h)]
    graph1 = DirectedGraph(vertexes, edges)
    components = strongly_connected_components(graph1)
    print(len(components))
    #for component in components:








