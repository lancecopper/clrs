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
class NameVertex(Vertex):
    def __init__(self, name):
        self.name = name
class Edge(Structure):
    _fields = ['u', 'v']
    _fieldtypes = [Vertex, Vertex]
    def __init__(self, u, v):
        '''
        if (u.x, u.y, u.z) == (v.x, v.y, v.z):
            raise ValueError("two endpoints of Edge object\
                has the same coordinate")
        '''
        super(Edge, self).__init__(u, v)
class Graph(Structure):
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
class UnDirectedGraph(Graph):
    _fields = ['u', 'v']
    #_vertexes = []
    #_edges = []
    def adj(self, v):
        adj_vertexes = []
        for edge in self._edges:
            if v is edge.v:
                adj_vertexes.append(edge.u)
            if v is edge.u:
                adj_vertexes.append(edge.v)
        return adj_vertexes
class DirectedGraph(Graph):
    def adj(self, v):
        adj_vertexes = []
        for edge in self._edges:
            if v is edge.u:
                adj_vertexes.append(edge.v)
        return adj_vertexes



