"""motif class"""

import numpy as np
import networkx as nx


class motifs:
    """Define motif subgraph"""

    def __init__(self, name="triangle", directed=False, nxmotif, **kwargs):
        """Create a motif with an nxsubgraph"""
        self.name = name
        self.directed = directed
        self.m = nxmotif  # nx subgraph

    def populate_coocurrence(coo_dict, nxgraph, additive=True):
        for base in nxgraph:
