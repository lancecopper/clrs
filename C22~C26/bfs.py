from collections import deque
from graph import Vertex, Edge, UnDirectedGraph

def bfs(g, s):
    temp_v = list(g.get_v())
    temp_v.remove(s)
    for u in temp_v:
        u.color = "white"
        u.d = float("inf")
        u.parent = None
    s.color = "gray"
    s.d = 0
    s.p = None
    q = deque()
    q.append(s)
    while len(q):
        u = q.popleft()
        for v in g.adj(u):
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.parent = u
                q.append(v)
        u.color = "black"
def print_path(g, s, v):
    if v is s:
        print ("vertex", s.name, end=' ')
    elif v.parent is None:
        print ("no path from", s, "to", v, "exists")
    else:
        print_path(g, s, v.parent)
        print("vertex", v.name, end=' ')

if __name__ == "__main__":
    v = []
    for i in range(8):
        temp = Vertex(i,i,i)
        temp.name = i
        v.append(temp)

    e = [ Edge(v[0], v[1]), Edge(v[0], v[4]), Edge(v[1], v[5]), Edge(v[2], v[3]),
          Edge(v[2], v[5]), Edge(v[2], v[6]), Edge(v[3], v[6]), Edge(v[3], v[7]),
          Edge(v[5], v[6]), Edge(v[6], v[7]) ]

    g = UnDirectedGraph(v, e)
    bfs(g, v[1])

    n_root = list(v)
    n_root.remove(v[1])

    for vertex in n_root:
        print("path from vertex", v[1].name, "to vertex", vertex.name)
        print_path(g, v[1], vertex)
        print("\n")
        print("*******************\n")






















