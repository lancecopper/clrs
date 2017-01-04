from bfs import Vertex, Edge, Graph

def dfs(g):
	for u in g.get_v():
		u.color = "white"
		u.parent = None
	time = 0
	for u in g.get_v():
		if u.color == "white"
		dfs_visit(g, u)

def dfs_visit(g, u):
	time += 1
	u.d = time
	u.color = "gray"
	for v in g.adj(u):
		if v.color == "white":
			v.parent = u
			dfs_visit(g, v)
	u.color = "black"
	time += 1
	u.f = time






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






