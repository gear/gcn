"""motif class"""

import numpy as np
import networkx as nx
import utils


class motifs:
    """Define motif subgraph. There are two types of nodes in 
    a motif: anchored nodes and normal nodes. If the motif contains
    only normal nodes, motif co-occurrence count with match all
    possible cases. Otherwise motif co-occurrence count will match
    only the anchored nodes. Note that there can be exactly two
    anchored nodes."""

    def __init__(self, name="triangle", directed=False, adj_motif, **kwargs):
        """Create a motif with an nxsubgraph."""
        self.name = name
        self.directed = directed
        self.m = adj_motif  # adj matrix
        self.size = adj_motif.shape[0]
        self.anchors = None  # tuple of anchor nodes
        self.perms = utils.gen_matrix_permutations(adj_motif)  #set

    def anchor_connected(self):
        """Check if the anchors of the motif is connected."""
        if self.anchors:
            i, j = self.anchors
            if self.directed:
                return self.m[i][j] == 1 or self.m[j][i] == 1
            else:
                return self.m[i][j] == 1 
        else:
            return False 

    def populate_coocurrence(self, coo_dict, nxgraph, additive=True):
        """Fill the @param coo_dict with motif co-occurrence matrix.
        The graph is provided as NXGraph format @param nxgraph. @param
        additive=True means also counting the size 2 motif (add motif
        co-occurrence on top of adj-matrix)."""
        for nodes in nxgraph:
            if self.anchor_connected():
                pass  # TODO: Generate all size self.size subgraphs
            
