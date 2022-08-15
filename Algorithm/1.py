import numpy as np
from operator import itemgetter

a = np.array([3, 1, 2])
print(a.argsort())

b = [{'a': 1, 'b': 2}]
get_1 = itemgetter(1)
print(b[0][0])
