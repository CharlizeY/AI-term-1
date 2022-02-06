import numpy as np
from numpy import unravel_index

def closest_pair(coord_list):
    length = len(coord_list)
    dist = np.zeros(shape=(length, length))
    for i, t1 in enumerate(coord_list):
        for j, t2 in enumerate(coord_list):
            dist[i,j] = euclidean_dist(t1,t2)
    dist = np.where(dist > 0, dist, np.inf) # Convert all zero entries to infinity
    x, y = unravel_index(dist.argmin(), dist.shape)
    return set([coord_list[x], coord_list[y]])

def euclidean_dist(t1, t2):
    a1 = np.array(t1)
    a2 = np.array(t2)
    euc_dist = np.linalg.norm(a1-a2)
    return euc_dist
    

