# ----------------------------------------------------------
# ----------------------------------------------------------
# Challenge 2
# ----------------------------------------------------------
# ----------------------------------------------------------
## Goals:
'''
    *Implement the Graph ADT with an adjacency list.
    *Implement code to read in a graph from a text file to create
     an instance of the Graph ADT and use it's methods.
    *Update your Graph ADT code to use Breadth-first search to compute
     the shortest path between two provided vertices in your graph.
'''
# ----------------------------------------------------------
# Inputs:
'''
    * The graph_data.txt
    G
    1,2,3,4,5
    (1,2)
    (1,4)
    (2,3)
    (2,4)
    (2,5)
    (3,5)
'''
# ----------------------------------------------------------
# Outputs:
'''
    Vertices in shortest path: 1,2,5
    Number of edges in shortest path: 3
'''

# ----------------------------------------------------------
# AbstractDataType origin
# ----------------------------------------------------------

# from graph import Graph

# ----------------------------------------------------------
# Main functions required to accomplish the Goal
# ----------------------------------------------------------

def make_graph(data):
    graph_network = Graph()
    for vertex in vertexes_of_data(data):
        graph_network.add_vertex(vertex)
    
    for adjacency_list in data[2:]:
        clean_adjacency_list = adjacency_list.rstrip().replace('(', '').replace(')', '').split(',') 
    return clean_adjacency_list 
    pass



# ----------------------------------------------------------
# Helper functions 
# ----------------------------------------------------------

def vertexes_of_data(data):
    return data[1].rstrip().split(',')

def _iter_lists_in_data(data):
    # adjacency_lists = []
    for adjacency_list in data[2:]:
        clean_adjacency_list = adjacency_list.rstrip().replace('(', '').replace(')', '').split(',') 
    return clean_adjacency_list

def open_file(file_name):
    file = open(file_name, 'r') 
    return file.readlines() 


# --------------------------------------------------------
# --------------------------------------------------------
# START OF SCRIPT
if __name__ == "__main__":

#  AbstractDataType needed
# --------------------------------------------------------

# Getting data ready
# --------------------------------------------------------
    data = open_file("graph_data.txt")
    print("This is the data file: ", data)
    
# Making the elements
# -------------------------------------------------------- 
    vertexes = vertexes_of_data(data)
    print("Vertices: ", vertexes, len(vertexes))


# Vertices: 4
# Edges: 4
# Edge List:
# (1,2,10)
# (1,4,5)
# (2,3,5)
# (2,4,7)

# Setting up the answer
    # for index in 

# --------------------------------------------------------
#  Data  
# --------------------------------------------------------

