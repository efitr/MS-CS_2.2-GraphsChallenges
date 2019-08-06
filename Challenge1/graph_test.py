# ----------------------------------------------------------
# ----------------------------------------------------------
# Test for a Graph AbstractDataType class 
# ----------------------------------------------------------
# ----------------------------------------------------------

# Components:
'''
    * Test suite for Vertex class made from the concept of an AdjacencyList DataStructure.
    * Test suite for a Graph AbstractDataType made out of the Vertex class.
'''

from graph import Vertex, Graph
import random
import unittest


class TestVertex(unittest.TestCase):
    
    # This tests an empty Vertex
    def test_init_(self):
        vertex = Vertex('A')
        self.assertEqual(vertex.links, {})
        self.assertEqual(vertex.num_links, 0)

    # This checks whether the links are bidirectional or unidirectional
    def test_add_link(self):
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        vertex_c = Vertex('C') 

        # This proofs that it is unidirectional
        vertex_a.add_link(vertex_b)
        self.assertEqual(vertex_a.num_links, 1)
        self.assertEqual(vertex_b.num_links, 0)
        self.assertEqual(vertex_c.num_links, 0)
        self.assertEqual(vertex_a.links, {vertex_b:0})
        self.assertEqual(vertex_b.links, {})

        vertex_c.add_link(vertex_a)
        self.assertEqual(vertex_a.num_links, 1)
        self.assertEqual(vertex_b.num_links, 0)
        self.assertEqual(vertex_c.num_links, 1)
        self.assertEqual(vertex_c.links, {vertex_a:0})
        self.assertEqual(vertex_a.links, {vertex_b:0})

    def test_get_links(self):
        vertex_a = Vertex('A')
        vertex_b = Vertex('B')
        vertex_c = Vertex('C')  
        vertex_d = Vertex('D')
        vertex_e = Vertex('E')
        vertex_f = Vertex('F')

        ## Links of A
        # Vertex 'A' => Vertex 'B'
        vertex_a.add_link(vertex_b)

        ## Links of B
        # Vertex 'A' => Vertex 'B'
        vertex_b.add_link(vertex_a)
        # Vertex 'B' => Vertex 'C'
        vertex_b.add_link(vertex_c) 

        ## Links of C
        # Vertex 'C' => Vertex 'D'
        vertex_c.add_link(vertex_d)

        ## Links of D
        # Vertex 'D' => Vertex 'E'
        vertex_d.add_link(vertex_e)

        ## Links of E
        # Vertex 'E' => Vertex 'F'
        vertex_e.add_link(vertex_f)


    def test_get_id(self):
        pass

    def test_get_edge_weight(self): 
        pass


class TestGraph(unittest.TestCase):

    def test_init_(self):
        pass

    def test_add_vertex(self):
        pass

    def test_get_vertex(self):
        pass

    def test_add_edge(self):
        pass

    def test_get_vertices(self):
        pass

    def test_iter_(self):
        pass