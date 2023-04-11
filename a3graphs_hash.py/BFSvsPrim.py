import random

"""Using matrix due to dense graph & edges needing to be weighted"""

""" part 1 is making randomized graph"""
""" part 2 is using BFS and Prim's algorithm to calculate which one ends with a lower weight"""


class Vertex:
    def __init__(self, n):
        self.vertexval = n


class Graph:
    # vertices has the name as the key and the object as the value, edges is the matrix, edge_indices to locate index of edgewhen given name as key
    vertices = {}
    edges = []
    edge_indices = {}

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
        n = 10
        for i in range(2, n):
            S = []
            x = random.randint(1, i-1)
            for j in range(x):
                S.append(random.randint(1, i-1))
            for num in S:
                self.add_vertex(Vertex(num))
                self.add_vertex(Vertex(i))
                self.add_edge(num, i, random.randint(10, 100))

    "-----part2--------------------------------"

    def print_graph(self):
        print("Adjacency Matrix:")
        for row in self.edges:
            print(row)

        print("\nVertices:")
        for vertex, index in self.edge_indices.items():
            print(f"{vertex}: {index}")


# Create a new graph
g = Graph()
g.randomgeneration()
g.print_graph()
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
