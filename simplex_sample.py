# uniform sampling from a unit simplex
import numpy as np

import nmslib

def sample(k, n):
    """
    Takes n uniformly distributed samples from a k-dimensional unit simplex.

    Source: https://www.cs.cmu.edu/~nasmith/papers/smith+tromble.tr04.pdf
    """
    # we have a simplex of dimensionality k.
    # sample k-1 real values in [0,1]
    # sort these values, appending 0 and 1
    # let y_i = x_i - x_{i-1}
    # y will be uniformly distributed in the simplex.
    x = np.hstack([np.zeros((n, 1)), np.random.rand(n, k-1), np.ones((n, 1))])
    x.sort()
    y = x[:, 1:] - x[:, :-1]
    return y

def data_sample(w, s_sample):
    """
    Given a (k, n) matrix of points on a k-dimensional simplex,
    and a (m, k) array of random samples from the k-dimensional simplex,
    this returns an array of m indices, where the i-th index is the index of
    the point in w closest to the i-th sample.
    """
    index = nmslib.init(method='hnsw', space='cosinesimil')
    index.addDataPointBatch(w.T)
    index.createIndex()
    neighbors = index.knnQueryBatch(s_sample, k=1, num_threads=4)
    indices = [neighbors[0][0] for n in neighbors]
    return np.array(indices)
