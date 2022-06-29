import pandas as pd
import numpy as np
import networkx as nx
import random


def get_graph(name="karate"):
    if name == "karate":
        G = nx.karate_club_graph()
        #bb = nx.edge_betweenness_centrality(G, normalized=True)
        #nx.set_edge_attributes(G, bb, "weights")
    else: 
        G = None
    return G

def get_all_weights(G):
    weights = []
    for edge in list(G.edges(data=True)):
        if edge[-1]['weight'] < 0:
            print(edge[-1]['weight'])
        weights.append(edge[-1]['weight'])    
    return weights


def get_sample_path(G, weights):
    sampled_edge_weights ={}
    for edge in G.edges:
        sampled_edge_weights[edge] = random.choice(weights)

    nx.set_edge_attributes(G, sampled_edge_weights, "sampled_weights")   

    path = nx.shortest_path(G,source=14,target=11, weight="sampled_weights")

    return path    


def get_median_path(G, weights, num_samples = 10):
    sampled_edge_weights ={}
    for edge in G.edges:
        sampled_weights = []
        for _ in range(num_samples):
            sampled_weights.append(random.choice(weights))
        sampled_edge_weights[edge] = np.median(sampled_weights)

    nx.set_edge_attributes(G, sampled_edge_weights, "median_weights")   

    path = nx.shortest_path(G,source=14,target=11, weight="median_weights")

    return path    


def get_median_and_sampled_paths(G, weights, num_samples = 10):
    median_edge_weights = {}
    sampled_edge_weights = {}
    for edge in G.edges:
        sampled_edge_weights[edge] = []
        for _ in range(num_samples):
            sampled_edge_weights[edge].append(random.choice(weights))
        median_edge_weights[edge] = np.median(sampled_edge_weights[edge])
    
    nx.set_edge_attributes(G, median_edge_weights, "median_weights") 
    median_path = nx.shortest_path(G,source=14,target=11, weight="median_weights")
    
    sample_paths = []
    for i in range(num_samples):
        edge_weight_sample = {edge: sampled_edge_weights[edge][i] 
                                for edge in sampled_edge_weights.keys()}

        nx.set_edge_attributes(G, edge_weight_sample, "edge_weight_sample") 
        sample_path = nx.shortest_path(G,source=14,target=11, weight="edge_weight_sample")
        sample_paths.append(sample_path)
    
    return median_path, sample_paths

        

