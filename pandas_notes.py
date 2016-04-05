import pandas as pd
import numpy as np

xs = pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4])

pd.cut(xs, bins=[0, 1, 2, 3, 4])
pd.cut(xs, bins=[0, 1, 2, 3, 4], labels=["one", "two", "three", "four"])

x1 = pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
pd.cut([.2, 1.4, 2.5, 6.2, 9.7, 2.1], 3, retbins=True)
x2 = pd.cut(pd.Series([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)

np.array_equal(pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3),
               pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)[0])
