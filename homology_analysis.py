import numpy as np
import ripser
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

# Compute the cohomology of the graph
rips = ripser.Rips()
dgms = rips.fit_transform(nx.adjacency_matrix(G))
coh1 = ripser.cohomology_persistence(dgms, coefficients=2)
dim1 = ripser.betti_numbers(coh1)
coh2 = ripser.cohomology_persistence(dgms, coefficients=3)
dim2 = ripser.betti_numbers(coh2)

# Print the first and second cohomology dimensions
print(f"First cohomology dimension: {dim1[1]}")
print(f"Second cohomology dimension: {dim2[2]}")
