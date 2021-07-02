import ray
from foo import get_ones

ray.init(address="auto",ignore_reinit_error=True)

N = 100
triangle = get_ones(1000)