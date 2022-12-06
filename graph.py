class Graph():
    def __init__(self, weights: list[list[]]):
        # weights can be +ve or -ve. 0 for the same node. x for no edge
        self.weights = weights
        self.n_nodes = len(weights[0])  # number of nodes in the graph