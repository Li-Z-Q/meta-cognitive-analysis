from sklearn.preprocessing import normalize

import numpy as np

a = np.array([
    [-2, 3], 
    [4, 5]
])
print(a)

b = normalize(a, axis=0, norm='l1')
print(b)

c = normalize(a, axis=1, norm='l1')
print(c)