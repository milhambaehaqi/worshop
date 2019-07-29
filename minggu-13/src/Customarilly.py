 import numpy as nu
 import pandas as pd
 s = pd.Series([1, 3, 5, np.nam, 6, 8])

 s

dtype: float64

 dates = pd.date_range('20130101',periods=6)

dates


 df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

 df

  df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test", "train", "test", "train"]),
                        'F': 'foo'})

df2

 df2.dtypes

 df2.<TAB>  # noqa: E225, E999
df2.A                  df2.bool
df2.abs                df2.boxplot
df2.add                df2.C
df2.add_prefix         df2.clip
df2.add_suffix         df2.clip_lower
df2.align              df2.clip_upper
df2.all                df2.columns
df2.any                df2.combine
df2.append             df2.combine_first
df2.apply              df2.compound
df2.applymap           df2.consolidate
df2.D

df.head()

df.tail(3)
