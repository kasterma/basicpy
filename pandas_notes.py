import pandas as pd
import numpy as np

# Series

s = pd.Series([1,3,5,np.nan,6,8])
t = pd.Series([2,3,1,2,np.nan,6])

ss = pd.Series([1,3,5,np.nan,6,8], index=range(6))
tt = pd.Series([2,3,1,2,np.nan,6], index=range(5, -1, -1))

pd.date_range('20160307', periods=3, freq='5H')

s1 = pd.Series([1,2,3], index=[3,4,5])
s2 = pd.Series([11,22,33], index=[4,5,6])
s1 + s2

pd.Series({"a": 1, "b": 2})
pd.Series({"a": 1, "b": 2}, index=["a", "b"])
pd.Series({"a": 1, "b": 2}, index=["a", "b", "c"])
pd.Series({"a": 1, "b": 2}, index=["a", "b", "b"])
pd.Series({"a": 1, "b": 2}, index=["a", "c", "b"])

s3 = pd.Series({"a": 1, "b": 2}, index=["a", "c", "b"])
s3["a"]
s3['d']           # KeyError
s3.get("d")       # None
s3.get("d", 666)  # 666

np.exp(s3)

s4 = s3.rename("hello")

# Data Frame

df1 = pd.DataFrame({"a": s1, "b": s2})
df1
df1.axes

x1 = pd.DataFrame(s1, columns=["a"])
x1
x1["b"] = s2
x1
x1.add(pd.DataFrame({"a": s2}))
x1 + pd.DataFrame({"a": s2})

pd.DataFrame(x1)
pd.DataFrame(x1, columns=["one", "a"])
pd.DataFrame(x1, columns=["one", "a"], index=[1,2,3,4])

df11 = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
              ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
              ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
              ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
              ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})


dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df.dtypes

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })

df2.head(2)
df.index

df['20130102':'20130104']

df2 = df.copy()
df2['E'] = ['one', 'one','two','three','four','three']

s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))

df = pd.DataFrame({'A' : ['foo', 'bar', 'foo', 'bar',
                          'foo', 'bar', 'foo', 'foo'],
                   'B' : ['one', 'one', 'two', 'three',
                          'two', 'two', 'one', 'three'],
                   'C' : np.random.randn(8),
                   'D' : np.random.randn(8)})
df.dtypes

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz',
                     'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two',
                     'one', 'two', 'one', 'two']]))
rng = pd.date_range('1/1/2012', periods=100, freq='S')

xs = pd.Series([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 4])

pd.cut(xs, bins=[0, 1, 2, 3, 4])
pd.cut(xs, bins=[0, 1, 2, 3, 4], labels=["one", "two", "three", "four"])

x1 = pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)
pd.cut([.2, 1.4, 2.5, 6.2, 9.7, 2.1], 3, retbins=True)
x2 = pd.cut(pd.Series([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)

np.array_equal(pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3),
               pd.cut(np.array([.2, 1.4, 2.5, 6.2, 9.7, 2.1]), 3, retbins=True)[0])

i1 = pd.Index([[1,1,2],[1,2,3]])
pd.Series(["a", "b"], index=i1)
pd.DataFrame({"a": ["a", "b"]}, index=i1)

# http://pandas.pydata.org/pandas-docs/stable/merging.html#database-style-dataframe-joining-merging

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                   index=[0, 1, 2, 3])

df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                   index=[4, 5, 6, 7])


df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

frames = [df1, df2, df3]

pd.concat(frames)

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                   index=[8, 9, 10, 11])

pd.concat([df1[["A", "B"]], df2, df3], axis=0)
pd.concat([df1[["A", "B"]], df2, df3], axis=1)
pd.concat([df1[["A", "B"]], df2, df3], axis=0, verify_integrity=True)
pd.concat([df1[["A", "B"]], df2, df3], join="inner")
xx = pd.concat([df1[["A", "B"]], df2, df3], join_axes=[pd.Index(["A", "B", "C"])])


xx = pd.concat(frames, keys=['x', 'y', 'z'])

df11 = pd.DataFrame(np.random.randint(0, 10, size=10).reshape((5, 2)),
                    index=[1, 2, 3, 4, 5],
                    columns=["a", "b"])

df11
df11.assign(c=lambda x: x.a + x.b)
df11.assign(c=lambda x: x.a + x.b).plot(kind='scatter', x="a", y="b")

df11.dot(df11.T)
df11.T.dot(df11)

# MultiIndex

mi1 = pd.MultiIndex.from_product([['x', 'y', 'z'], ['a', 'b']], names=['one','two'])
mis = pd.Series([1,2,3,4,5,6], index=mi1)

