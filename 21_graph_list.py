class Graph:
    def __init__(self, vno):
        self.vertex_count = vno
        self.adj_list = { v:[] for v in range(vno)}


    def add_edge(self, u, v, weight = 1):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u].append((v, weight))
            self.adj_list[v].append((u, weight))
        else:
            print('invalid vertax')

    def remove_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            self.adj_list[u] = [(vertax , weight) for vertax, weight in self.adj_list[v] if vertax is not u]
            self.adj_list[v] = [(vertax , weight) for vertax, weight in self.adj_list[u] if vertax is not v] 
        else:
            print('invalid vertax')

    def has_edge(self, u, v):
        if 0<=u<self.vertex_count and 0<=v<self.vertex_count:
            return any(vertax == v for vertax , x in self.adj_list[u])
        else:
            print('invalid vertax')

    def print_add_list(self):
        for vertax, n in self.adj_list.items():
            print('v', vertax, ":", n)

g = Graph(5)
g.add_edge(0,1)
g.add_edge(0,1)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_add_list()

