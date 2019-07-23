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


# ----------------------------------------------------------
# Helper functions 
# ----------------------------------------------------------


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
