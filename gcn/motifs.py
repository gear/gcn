"""motif class"""

import numpy as np
import networkx as nx


class motifs:
    """Define motif subgraph. There are two types of nodes in 
    a motif: anchored nodes and normal nodes. If the motif contains
    only normal nodes, motif co-occurrence count with match all
    possible cases. Otherwise motif co-occurrence count will match
    only the anchored nodes. Note that there can be exactly two
    anchored nodes."""

    def __init__(self, name="triangle", directed=False, nxmotif, **kwargs):
        """Create a motif with an nxsubgraph"""
        self.name = name
        self.directed = directed
        self.m = nxmotif  # nx graph
        self.anchors = []  # list of anchor nodes

    def populate_coocurrence(self, coo_dict, nxgraph, additive=True):
        """Fill the @param coo_dict with motif co-occurrence matrix.
        The graph is provided as NXGraph format @param nxgraph. @param
        additive=True means also counting the size 2 motif (add motif
        co-occurrence on top of adj-matrix)."""
        for nodes in nxgraph:
            for other_nodes in nxgraph:
                if nodes == other_nodes:
                    continue
                 
        

                 
