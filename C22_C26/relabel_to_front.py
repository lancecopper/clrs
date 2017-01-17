from push_relabel import StreamEdge, calc_cf, push, relabel, initialize_preflow
from graph import DirectedGraph

class StreamVertex():
    def __init__(self, name):
        self.name = name
        self.e = 0
        self.h = 0
        self.n = None
        self.current = None
class StreamGraph(DirectedGraph):
    def __init__(self, s, t, vertexes, edges):
        self._residual_edges = edges
        self.s = s
        self.t = t
        for u in vertexes:
            temp_r_adj_edges = []
            temp_adj_edges = []
            temp_r_adj_vertexes = []
            temp_adj_vertexes = []
            for edge in edges:
                if u is edge.u:
                    temp_adj_edges.append(edge)
                    temp_adj_vertexes.append(edge.v)
                    temp_r_adj_edges.append(edge)
                    temp_r_adj_vertexes.append(edge.v)
                elif u is edge.v:
                    temp_r_adj_edges.append(edge)
                    temp_r_adj_vertexes.append(edge.u)
            u.adj_edges = temp_adj_edges
            u.adj_vertexes = temp_r_adj_vertexes
            u.r_adj_edges = temp_r_adj_edges
            u.r_adj_vertexes = temp_r_adj_vertexes
            u.n = LinkedList(temp_r_adj_vertexes)
        super(StreamGraph, self).__init__(vertexes, edges)
class LinkedList():
    def __init__(self, nodes):
        self.nodes = nodes
        self.head = None
        self._next = dict()
        self.head = nodes[0]
        for i in range(1, len(nodes)):
            self._next[nodes[i - 1]] = nodes[i]
        self._next[nodes[i]] = None
    def move_front(self, u):
        for k,v in self._next.items():
            if v is u:
                self._next[k] = self._next[v]
                self._next[v] = self.head
                self.head = v
                break
    def next(self, node):
        return self._next[node]

def discharge(u, g):
    while u.e > 0:
        v = u.current
        if v is None:
            relabel(u, g)
            u.current = u.n.head
        elif calc_cf(u, v, g) > 0 and u.h == v.h + 1:
            push(u, v, g)
        else:
            u.current = u.n.next(v)
    
def relabel_to_front(g, s, t):
    initialize_preflow(g, s)
    vertexes = g.get_v().copy()
    vertexes.remove(g.s)
    vertexes.remove(g.t)
    l = LinkedList(vertexes)
    for u in vertexes:
        u.current = u.n.head
    u = l.head
    while u is not None:
        old_height = u.h
        discharge(u, g)
        if u.h > old_height:
            l.move_front(u)
        u = l.next(u)
        
if __name__ == "__main__":
    temp_globals = globals()
    vertexes = []
    for vertex_name in "sxyzt":
        temp_globals[vertex_name] = StreamVertex(vertex_name)
        vertexes.append(eval(vertex_name))
    edges = [StreamEdge(s, x, 12), StreamEdge(s, y, 14), 
             StreamEdge(x, y, 5), StreamEdge(x, t, 16),
             StreamEdge(y, z, 8), StreamEdge(z, x, 7),
             StreamEdge(z, t, 10)]
    graph1 = StreamGraph(s, t, vertexes, edges)
    relabel_to_front(graph1, s, t)
    if not (s.e + t.e):
        print("the overall flow is {}".format(t.e))
    else:
        print(s.e, t.e)
        print("ERROR! flow from s to t is not conserved!")
    for vertex in vertexes:
        print(vertex.name, vertex.e)
    for edge in edges:
        print("flow of edge {} -> {} is {}".format(edge.u.name, edge.v.name, edge.flow))




