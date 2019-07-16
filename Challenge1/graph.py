# ----------------------------------------------------------
# ----------------------------------------------------------
# Graph || Network AbstractDataType, made with Vertex || 
# Node || AdjacencyList DataStructure
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
# ----------------------------------------------------------
# Class Vertex or Node
# ----------------------------------------------------------