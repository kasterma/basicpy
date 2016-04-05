import numpy as np

x1 = np.array([1,2,3])
x2 = np.array([1,1,1])

np.array_equal(x1, x1)   # True if two arrays have the same shape and elements, False otherwise.
np.array_equal(x1, x2)

np.array_equiv(x1, x1)   # Returns True if input arrays are shape consistent and all elements equal.
np.array_equiv(np.vstack([x1, x1, x1]), x1) # True, broadcasting works in the dim that is equal to 1
np.array_equiv(np.hstack([x1, x1, x1]), x1)   # False

np.array_equiv(np.hstack([x1, x1, x1]).reshape((3, 3)), x1)


np.hstack([x1, x1, x1, x1]).reshape((2, -1, 2))
