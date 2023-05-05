import numpy as np
import gudhi
import networkx as nx

# Load gene expression data
data = np.loadtxt("data/gene_expression_data.txt")

# Compute the pairwise correlation matrix
corr_matrix = np.corrcoef(data.T)

# Create a weighted graph from the correlation matrix
G = nx.Graph()
for i in range(corr_matrix.shape[0]):
    for j in range(i + 1, corr_matrix.shape[1]):
        weight = abs(corr_matrix[i, j])
        if weight > 0:
            G.add_edge(i, j, weight=weight)

# Construct the simplicial complex from the graph
simplicial_complex = gudhi.SimplexTree()
for node in G.nodes():
    simplicial_complex.insert([node])
for edge in G.edges():
    weight = G[edge[0]][edge[1]]["weight"]
    simplicial_complex.insert([edge[0], edge[1]], filtration=weight)

# Compute the persistent homology of the simplicial complex
persistence = simplicial_complex.persistence()

# Print the persistence diagram
print(persistence)
