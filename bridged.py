from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


class GraphBridge:

    def __init__(self):
        self.vertices = 0
        self.graph = defaultdict(list)
        self.edges = []

    def add_edge(self, u, v):
        self.vertices += 1
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.edges.append((u,v))

    def all_visited(self, visited):
        for i in visited:
            if not i:
                return False
        return True

    def extract_cycle(self, prec, starting, current):
        cycle = [starting, current]
        while prec[current] != starting:
            cycle.append(prec[current])
            current = prec[current]
        cycle.append(starting)
        return cycle

    def extract_edges_from_vertices(self, cycles):
        edges = []
        for cycle in cycles:
            for index in range(len(cycle)-1):
                edges.append((cycle[index], cycle[index+1]))
        return edges

    def equal_edge(self,bridge_edge,cycle_edge):
        count = 0
        for bridge in bridge_edge:
            for cycle in cycle_edge:
                if bridge == cycle:
                    count+=1
        return count==2

    def get_bridges(self,bridges, cycle_edges):
        bridge_edges = bridges.copy()
        for bridge in bridges:
            for cycle_edge in cycle_edges:
                if self.equal_edge(bridge, cycle_edge):
                    bridge_edges.remove(bridge)
        return bridge_edges

    def dfs(self):
        prec = [None] * (self.vertices + 1)
        visited = [False] * (self.vertices + 1)
        nr = [None] * (self.vertices + 1)
        cycles = []
        bridges = self.edges
        prec[1] = 1
        nr[1] = 1
        visited[0] = True
        visited[1] = True
        current = 1
        current_nr = 1

        while not self.all_visited(visited):
            for neighbour in my_graph.graph[current]:
                if visited[neighbour] and nr[current] > nr[neighbour] and prec[current] != neighbour:
                    cycles.append(self.extract_cycle(prec, neighbour, current))
                if not visited[neighbour]:
                    visited[neighbour] = True
                    prec[neighbour] = current
                    current_nr += 1
                    nr[neighbour] = current_nr
                    current = neighbour
                    break
                if visited[neighbour] and neighbour == my_graph.graph[current][len(my_graph.graph[current]) - 1]:
                    current = prec[current]

        return prec, cycles, self.get_bridges(bridges,self.extract_edges_from_vertices(cycles))


my_graph = GraphBridge()
my_graph.add_edge(1, 2)
my_graph.add_edge(2, 3)
my_graph.add_edge(2, 4)
my_graph.add_edge(3, 5)
my_graph.add_edge(4, 5)
my_graph.add_edge(5, 8)
my_graph.add_edge(8, 7)
my_graph.add_edge(8, 9)
my_graph.add_edge(7, 6)


prec, cycles, bridges = my_graph.dfs()
print(prec)
print(cycles)
print(bridges)

# G = nx.Graph()
# G.add_edges_from([(1,2),(2,3), (2,4), (3,5), (4,5), (5,8), (8,7), (8,9), (7,6)])
# nx.draw(G)
# plt.show()
