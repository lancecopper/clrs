from clrs.C22_C26.graph import UnDirectedGraph
def approx_vertex_cover(g):
    pass


def greedy_set_cover(x, f):
    sort f with length      #|F|lg|F|
    sort each fs in f       #sigma(fs in f) |fs|lg|fs|
    u = x
    delta = []
    while len(u) > 0:       #sigma(fs in f) |fs|
        s = maximum(f)
        for i in s:                
            for fs in f:
                if i in fs:
                    fs.length -= 1


