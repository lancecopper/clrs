from collections import deque


class Structure():
    _fields = []
    _fieldtypes = []
    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))
        if len(self._fieldtypes) > 0:
            for value, fieldtype in zip(args, self._fieldtypes):
                if not isinstance(value, fieldtype):
                    raise TypeError("Expected arguments: {}".format(self._fieldtypes))
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


class Vertex(Structure):
    _fields = ['x', 'y', 'z']
    color = None
    parent = None
    d = None
    f = None
    name = None

    '''
    _fieldtypes = [float, float, float]
    
    def __init__(self, x, y, z = 0):
        self.x = x
        self.y = y
        self.z = z
    '''


class Edge(Structure):
    _fields = ['u', 'v']
    _fieldtypes = [Vertex, Vertex]

    def __init__(self, u, v):
        if (u.x, u.y, u.z) == (v.x, v.y, v.z):
            raise ValueError("two endpoints of Edge object\
                has the same coordinate")
        super(Edge, self).__init__(u, v)



class Graph(Structure):
    
    _fields = ['u', 'v']
    _vertexes = []
    _edges = []
    
    def __init__(self, vertexes, edges):
        self._vertexes = vertexes
        self._edges = edges

    def add_vertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("method <add_vertex> expected <vertex> type argument.")
        self._vertexes.append(vertex)

    def add_vertexes(self, vertexes):
        for vertex in vertexes:
            self.add_vertex(vertex)

    def add_edge(self, edge):
        if not isinstance(edge, Edge):
            raise TypeError("method <add_edge> expected <Edge> type argument.")
        _edges.append(edge)
        if edge.u not in _edges:
            self.add_vertex(edge.u)
        if edge.v not in _edges:
            self.add_vertex(edge.v)

    def add_edge(self, edges):
        for edge in edges:
            self.add_edge(edge)

    def get_v(self):
        return self._vertexes

    def get_e(self):
        return self._edges



class Directed_Graph(Graph):
    _fields = ['u', 'v']
    _vertexes = []
    _edges = []
    def adj(self, v):
        adj_vertexes = []
        for edge in self._edges:
            if v is edge.v:
                adj_vertexes.append(edge.u)
            if v is edge.u:
                adj_vertexes.append(edge.v)
        return adj_vertexes


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


    g = Directed_Graph(v, e)
    bfs(g, v[1])

    n_root = list(v)
    n_root.remove(v[1])

    for vertex in n_root:
        print("path from vertex", v[1].name, "to vertex", vertex.name)
        print_path(g, v[1], vertex)
        print("\n")
        print("*******************\n")






















