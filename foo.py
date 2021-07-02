import ray
import numpy as np

def baz(M):
    return 2*M

@ray.remote
def bar(n):
    M = np.random.rand(n,n)
    v = np.ones(n)
    M = np.linalg.multi_dot((M,M,M,M,v))
    X = baz(M)
    return X

def get_ones(n):
    ref = [bar.remote(n) for _ in range(n)]
    one_mat = ray.get(ref)
    return one_mat