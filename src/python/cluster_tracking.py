import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
import networkx as nx
import markov_clustering as mc
import matplotlib.pyplot as plt

def construct_similarity_matrix(age):
    # Construction of the similarity matrix at given age
    pres_tab = pd.read_csv(f"data/input/pres_{age}.csv", sep=";")
    
    # Computation of the Cosine similarity between patients 
    cos_DF = pd.DataFrame(cosine_similarity(pres_tab),
                          columns=pres_tab.index.astype("str"),
                          index=pres_tab.index.astype("str"))
    
    # Save
    cos_DF.to_parquet(f"data/output/cosine_{age}.gzip", compression="gzip")
    return cos_DF

def cluster_patient_network(age):
    # Similarity matrix at given age
    cos_tab = pd.read_parquet(f"data/output/cosine_{age}.gzip")
    cos_tab.values[np.arange(cos_tab.shape[0]), np.arange(cos_tab.shape[0])] = 0  # We set the diagonal of the matrix to 0
    cos_tab.mask(cos_tab < 0.7, 0, inplace=True)  # We filtered the matrix with the chosen Cosine similarity threshold = 0.7

    # Network construction
    G = nx.from_pandas_adjacency(cos_tab)

    # Component extraction
    Gcc1 = sorted(nx.connected_components(G), key=len, reverse=True)[0]  # The largest connected component
    Gcc2 = sorted(nx.connected_components(G), key=len, reverse=True)[1:]  # The other connected components

    # Largest connected component network
    G = G.subgraph(Gcc1) 

    # Extractions of clusters from MCL algorithm applied to the largest connected component network
    mat = nx.to_scipy_sparse_matrix(G)
    mcl = mc.run_mcl(mat) 
    clust = mc.get_clusters(mcl)  # list of identified clusters
    pat = list(G.nodes())  # Patient IDs
    res = []
    for y in range(len(clust)):
        for j in clust[y]:
            res.append([pat[j], y+1])  # Patient ids + cluster they belong to

    # Extraction of clusters from the other connected components: each connected component represent a cluster
    y = y + 2  # next cluster
    if len(Gcc2) != 0:
        for g in Gcc2:
            for pat in g:
                res.append([pat, y])  # Patient ids + cluster they belong to
            y = y + 1

    clust_data = pd.DataFrame(res, columns=['Patient', 'cluster'])

    # Save
    clust_data.to_csv(f"data/output/clusters_net_{age}.csv", sep=";", index=False)
    return clust_data

def cluster_raw_data(age, n_clusters):
    # Table of reimbursements at given age
    pres_tab = pd.read_csv(f"data/input/pres_{age}.csv", sep=";")

    # Kmeans applied with the optimal number of clusters identified for the given age
    KM = KMeans(n_clusters=n_clusters).fit(pres_tab.values)
    label = KM.labels_
    id_label = pres_tab.index
    res = []
    for j in range(len(label)):
        res.append([id_label[j], label[j]+1])  # Patient ids + cluster they belong
    clust_data = pd.DataFrame(res, columns=['Patient', 'cluster'])

    # Save
    clust_data.to_csv(f"data/output/clusters_raw_{age}.csv", sep=";", index=False)
    return clust_data

def main():
    # Example usage
    ages = range(60, 70)  # Assuming we're analyzing ages 60 to 70
    
    # Construct similarity matrices for all ages
    for age in ages:
        construct_similarity_matrix(age)
    
    print(f"Similarity matrix completed for all ages.")
    
    # Cluster patient networks for all ages
    for age in ages:
        cluster_patient_network(age)
    
    print(f"Clustering on patients network completed for all ages.")
    
    # Cluster raw data for all ages
    # Note: You'll need to determine the optimal number of clusters for each age
    # This example uses a fixed number (6) for demonstration purposes
    for age in ages:
        cluster_raw_data(age, n_clusters=6)
    
    print(f"Clustering on raw data completed for all ages.")
    
    print("Clustering analysis completed for all ages.")

if __name__ == "__main__":
    main()
