import random

"""Using matrix due to dense graph & edges needing to be weighted. 

Correction: it is sparse graph, continuing with matrix even though it is inefficient"""

""" part 1 is making randomized graph"""
""" part 2 is using BFS and Prim's algorithm to calculate which one ends with a lower weight"""


class Vertex:
    def __init__(self, n):
        self.vertexval = n


class Graph:
    # vertices has the name as the key and the object as the value, edges is the matrix, edge_indices to locate index of edge when given name as key
    vertices = {}
    edges = []
    edge_indices = {}
    n = 10

    """ chose to use matrix because after I read the instructions I thought it was going to be a dense graph, but it is sparse"""

    def add_vertex(self, vertex):
        # check if vertex is already in graph
        if isinstance(vertex, Vertex) and vertex.vertexval not in self.vertices:
            # adds to dictionary where key is vertex name and value is vertex node/object
            self.vertices[vertex.vertexval] = vertex
            # need new row for each vertex added

            # makes row
            for row in self.edges:
                row.append(0)
            # makes another column for matrix
            self.edges.append([0] * (len(self.edges) + 1))
            # make vertex we are adding the correspond to last index of our matrix
            self.edge_indices[vertex.vertexval] = len(self.edge_indices)
            return True

        else:
            return False

    def add_edge(self, i, j, weight):
        # check if vertices are in dict of vertices
        if i in self.vertices and j in self.vertices:
            # self.edges is matrix, indices is dictionary where vertex name is key & index is value. Value will be output
            # So it adds weight to corresponding 2x2 point on matrix of the two vertices
            self.edges[self.edge_indices[i]][self.edge_indices[j]] = weight
            self.edges[self.edge_indices[j]][self.edge_indices[i]] = weight
            return True
        else:
            return False

    def randomgeneration(self):
        for i in range(2, self.n):
            S = []
            x = random.randint(1, i-1)
            for j in range(x):
                S.append(random.randint(1, i-1))
            for num in S:
                self.add_vertex(Vertex(num))
                self.add_vertex(Vertex(i))
                self.add_edge(num, i, random.randint(10, 100))

    "-----part2--------------------------------"

    def Prims(self):

        S = []
        T = []
        Q = []
        D = {}
        # add each vertex to Q
        for vertex, index in self.edge_indices.items():
            Q.append(vertex)
        # getting all edges paired with vertex coordinates & getting rid of repitions ex) 0,2 and 2,0
        for i in range(self.n-1):
            for j in range(self.n-1):
                weight = self.edges[i][j]
                if (j, i) not in D:
                    D[(i, j)] = weight
                else:
                    pass
        # pick random first vertice from Q for T
        x = random.randint(0, len(Q)-1)
        T.append(Q[x])
        Q.remove(Q[x])
        # sort D by value lowet to highest
        D = dict(sorted(D.items(), key=lambda item: item[1]))
        # implement prims
        while len(S) < self.n-1:
            print(S)
            for e in D:
                if e[0] in T and e[1] in Q:
                    S.append(D[e])
                    T.append(e[1])
                    Q.remove(e[1])
                    break
                elif e[1] in T and e[0] in Q:
                    S.append(D[e])
                    T.append(e[0])
                    Q.remove(e[0])
                    break
        print("Final edge values are", S)

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.edges:
            print(row)

        print("\nVertices:")
        for vertex, index in self.edge_indices.items():
            print(vertex)


# Create a new graph
g = Graph()
g.randomgeneration()
# g.print_graph()
g.Prims()
"""
# Add some vertices to the graph
g.add_vertex(Vertex('A'))
g.add_vertex(Vertex('B'))
g.add_vertex(Vertex('C'))
g.add_vertex(Vertex('D'))

# Add some edges to the graph
g.add_edge('A', 'B', 2)
g.add_edge('B', 'C', 3)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'A', 4)

# Print the graph
g.print_graph()
"""
