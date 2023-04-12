import random
import queue

"""Using matrix due to dense graph & edges needing to be weighted. 

Correction: it is sparse graph, continuing with matrix even though it is inefficient"""

""" part 1 is making randomized graph"""
""" part 2 is using BFS and Prim's algorithm to calculate which one ends with a lower weight"""


class Vertex:
    def __init__(self, n):
        self.vertexval = n
        self.added_queue = False


class Graph:
    # vertices has the name as the key and the object as the value, edges is the matrix, edge_indices to locate index of edge when given name as key
    vertices = {}
    edges = []
    edge_indices = {}
    n = 4

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
            self.add_vertex(Vertex(i))
            x = random.randint(1, i - 1)
            S = random.sample(range(1, i), x)
            for num in S:
                self.add_vertex(Vertex(num))
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
        # getting all edges paired with vertex coordinates & getting rid of repetitions ex) 0,2 and 2,0
        for i in range(self.n-1):
            for j in range(self.n-1):
                weight = self.edges[i][j]
                # +1 because it should represent the vertice value not the index of the vertice
                if weight != 0:  # check if the weight is non-zero
                    D[(i+1, j+1)] = weight

        # pick random first vertex from Q for T
        x = random.randint(0, len(Q)-1)
        T.append(Q[x])
        Q.remove(Q[x])
        # sort D by value lowest to highest
        D = dict(sorted(D.items(), key=lambda item: item[1]))

        # implement prim's algorithm
        """recall when we made the graph it was generated from 2 -> n, therefore our count of vertices in the graph
        will be n-1 since it start at 2. In my case n= 10, so 9 vertices therefore total amount of edges must be 8
        hence the len(S) < self.n-2, not len(S) < self.n"""
        while len(S) < self.n-2:
            for e in D:
                if e[0] in T and e[1] in Q and D[e] != 0:  # check if the edge weight is non-zero
                    S.append(D[e])
                    T.append(e[1])
                    Q.remove(e[1])
                    break
        print("Final edge values are", S)

    def BFS(self):
        q = queue.Queue()
        q.put(self.vertices[2])
        self.vertices[2].added_queue = True
        finalweight = []
        while q.empty() == False:
            neighbours = []
            x = q.get()
            for i in range(self.n - 1):
                if self.edges[i][x.vertexval - 1] != 0:
                    neighbours.append(self.vertices[i+1])
                for neighbour in neighbours:
                    if neighbour.added_queue == False:
                        q.put(neighbour)
                        neighbour.added_queue = True
                        print(type(neighbour.vertexval))
                        finalweight.append(
                            self.edges[x.vertexval-1][neighbour.vertexval - 1])
        print("Final edge values are", finalweight)

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.edges:
            print(row)


#        print("\nVertices:")
 #       for vertex, index in self.edge_indices.items():
  #          print(vertex)

# Create a new graph
g = Graph()
g.randomgeneration()
g.print_graph()
# g.Prims()
g.BFS()


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
