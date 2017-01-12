from graph import Vertex, Edge, DirectedGraph, NameVertex
from dfs import dfs
import random



def topological_sort(g):
    dfs(g)
    vertexes = g.get_v()
    quick_sort_final(vertexes, 0, len(vertexes) - 1)
    return vertexes

def quick_sort_final(vertexes, p, q):
    if p < q:
        r = partion(vertexes, p, q)
        quick_sort_final(vertexes, p, r)
        quick_sort_final(vertexes, r + 1, q)

def partion(vertexes, p, q):
    r = random.randint(p, q)
    vertexes[r], vertexes[q] = vertexes[q], vertexes[r]
    x = vertexes[q].f
    j = p - 1
    for i in range(p, q):
        if vertexes[i].f < x:
            j += 1
            vertexes[j], vertexes[i] = vertexes[i], vertexes[j]
    vertexes[j + 1], vertexes[q] = vertexes[q], vertexes[j + 1]
    return j + 1

if __name__ == "__main__":
    clothing = ["undershorts", "pants", "belt", "shirt",
                "tie", "jacket", "socks", "shoes", "watch"]
    vertexes = []
    for cloth in clothing:
        temp_locals = locals()
        temp_locals[cloth] = NameVertex(cloth)
        vertexes.append(eval(cloth))
    edges = [Edge(undershorts, pants), Edge(undershorts, shoes),
             Edge(pants, belt), Edge(pants, shoes), Edge(belt, jacket),
             Edge(shirt, tie), Edge(shirt, belt), Edge(tie, jacket),
             Edge(socks, shoes)]
    g = DirectedGraph(vertexes, edges)
    results = topological_sort(g)
    results.reverse()
    for result in results:
        #print(result.name, result.d, result.f)
        print(result.name, end = ', ')
    print()








