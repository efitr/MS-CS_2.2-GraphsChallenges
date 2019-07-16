# ----------------------------------------------------------
# ----------------------------------------------------------
# Graph || Network AbstractDataType, made with Vertex || 
# Node || AdjacencyList DataStructure
# ----------------------------------------------------------
# ----------------------------------------------------------

# Components:
'''
    **This is the components of the class for the Vertex Adjacent Lists DataStructure 
    and Graps AbstractDataTypes**
'''

## * Class Vertex or Node - Implemented with an Adjacency List DataStructure
'''
    init(  self , vertex  ) : "Here you only have to start the traits like the name and neighbors data" 
    add_neighbor(  self , vertex , weight=0  ) : "If the neighbor is not in there already, add the name 
                                                  to the dictionary"
    get_neighbors(  self  ) : "Return the dictionary property of the function"
    get_id(  self  ) : "Return the id property that is the same has the vertex information"
    get_edge_weight(  self , vertex  ) : "Return the weight of the given edge towards the vertex"
'''

## * Class Graph or Network - Implemented with a Vertex.
'''
    init(  self  ) : "It has dictionary with all the vertices and keeps track of the amount of Vertex or Nodes on it"
    add_vertex(  self , key  ) : "Add another element(vertex) to this Graph(Network) with the key(vertex_name) and return the vertex(new_node)"
    get_vertex(  self , key  ) : "Return the vertex if it belongs to the Graph(Network)"
    add_edge(  self , key1 , key2 , weight=0  ) : "Add an edge from vertex with key1 to vertex with key2 with a weight"
    get_vertices(  self  ) : "Return all the nodes that there might be on the Network(Graph)"
    iter(  self  ) : "Iterate through all the elements or until a sentinel is found"
'''

# ----------------------------------------------------------
# Class Vertex or Node, AdjacentList DataStructure
# ----------------------------------------------------------
class Vertex(object):
    def __init__(self, new_vertex):
    # "Here you only have to start the traits like the name and neighbors data" 
        # The name of the vertex is the id
        self.id = new_vertex
        # This will store 
        self.links = {}
        self.num_links = 0

    def add_link(self, vertex, weight=0):
    # "If the neighbor is not in there already, add the name to the dictionary"
        if vertex not in self.links:
            self.links[vertex] = weight
            self.num_links += 1
    

    def get_links(self):
    # "Return the dictionary property of the function"
        return self.links.keys()

    def get_id(self):
    # "Return the id property that is the same has the vertex information"
        return self.id

    def get_edge_weight(self, vertex):
    # "Return the weight of the given edge towards the vertex"
        return self.links[vertex]
 

# ----------------------------------------------------------
# Class Graph or Network
# ----------------------------------------------------------
class Graph(object):
    def __init__(self):
        self.vertex_network = {}
        self.num_vertexes = 0
        self.num_edges = 0

    def add_vertex(self, key):
        # Must fix, there is no collision control,
        # what if the key is already inside
        # What are the parameters for keys to be 
        # acceptable
        if key not in self.vertex_network:
            new_vertex = Vertex(key)
            self.vertex_network[key] = new_vertex
            self.num_vertexes += 1

        return self.vertex_network[key]
    
    def get_vertex(self, key):
        return self.vertex_network[key]

    def add_edge(self, from_vertex, to_vertex, weight=0):
    # If the vertex was not already on the network, add it
        if from_vertex not in self.vertex_network:
            self.add_vertex(from_vertex)
        if to_vertex not in self.vertex_network:
            self.add_vertex(to_vertex)

        self.vertex_network[from_vertex].add_link(self.vertex_network[to_vertex], weight)

    def get_vertices(self):
        """return all the vertices in the graph"""
        return self.vertex_network.keys()

    def __iter__(self):
        """Iterate over the vertex objects in the graph, to use sytax: for v in g"""
        return iter(self.vertex_network.values())
