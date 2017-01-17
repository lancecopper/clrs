from graph import DirectedGraph

class StreamEdge():
    #__slots__ = ['flow', 'capacity', 'u', 'v']
    def __init__(self, u, v, capacity):
        self.capacity = capacity
        self.flow = 0
        self.u = u
        self.v = v
class StreamVertex():
    def __init__(self, name):
        self.name = name
        self.e = 0
        self.h = 0
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
        super(StreamGraph, self).__init__(vertexes, edges)
def calc_cf(u, v, g):
    uv_edge = g.find_edge(u, v)
    if uv_edge:
        return uv_edge.capacity - uv_edge.flow
    else:
        uv_edge = g.find_edge(v, u)
        if uv_edge:
            return uv_edge.flow
        else:
            print(u.name, v.name)
            print("jajajaj")
            return None
def push(u, v, g):
    delta_f_uv = min(u.e, calc_cf(u, v, g))
    uv_edge = g.find_edge(u, v)
    if uv_edge:
        uv_edge.flow += delta_f_uv
    else:
        uv_edge = g.find_edge(v, u)
        uv_edge.flow -= delta_f_uv
    u.e = u.e - delta_f_uv
    v.e = v.e + delta_f_uv
def relabel(u, g):
    r_adj_vertexes = []
    for v in u.r_adj_vertexes:
        if calc_cf(u, v, g):
            r_adj_vertexes.append(v)
    min_h = float("inf")
    for vertex in r_adj_vertexes:
        if vertex.h < min_h:
            min_h = vertex.h
    u.h = 1 + min_h
def initialize_preflow(g, s):
    vertexes = g.get_v()
    edges = g.get_e()
    for v in vertexes:
        v.h = 0
        v.e = 0
    for edge in edges:
        edge.flow = 0
    s.h = len(vertexes)
    for edge in s.adj_edges:
        edge.flow = edge.capacity
        edge.v.e = edge.capacity
        s.e = s.e - edge.capacity


def generic_push_relabel(g, s):
#这里如果要实现O(1)时间复杂度的话，首先得保证能在O(1)时间找到
#vertex.e最大的vertex,因为无论是push还是relabel都需要e > 0, 
#其次还需要对每个点u维护这样一个数据结构:
#其中的元素是所有点v(满足cf(u, v) > 0)，
#且该数据结构支持extract_min操作，可以在O(1)时间内找出vertex.h最小的vertex。
    initialize_preflow(g, s)
    vertexes = g.get_v().copy()
    vertexes.remove(g.s)
    vertexes.remove(g.t)
    while True:
        end_flag = True
        for u in vertexes:
            if u.e > 0:
                end_flag = False
                break
        if end_flag:
            break
        else:
            r_adj_vertexes = []
            push_flag = False
            for v in u.r_adj_vertexes:
                print("travel u.r_adj_vertexes", v.name)
                if calc_cf(u, v, g) and u.h == v.h + 1:
                    print("push", u.name, v.name)
                    push(u, v, g)
                    push_flag = True
                    break
            if not push_flag:
                print("relabel", u.name)
                relabel(u, g)

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
    generic_push_relabel(graph1, s)
    if not (s.e + t.e):
        print("the overall flow is {}".format(t.e))
    else:
        print("ERROR! flow from s to t is not conserved!")
    for edge in edges:
        print("flow of edge {} -> {} is {}".format(edge.u.name, edge.v.name, edge.flow))




        





