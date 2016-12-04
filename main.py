import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def test():
    s = pd.Series([1,3,5,np.nan,6,8])
    print(s)
    print("")

    dates = pd.date_range('20130101', periods=4)
    print(dates)
    print("")

    df = pd.DataFrame(np.random.randn(4,4), index=dates, columns=list('ABCD'))
    print(df)
    print("")

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20130102'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["orange", "pencil", "plane", "compas"]),
                        'F': 'foo'})
    print(df2)
    print("")

    print(df2.dtypes)
    print("")

if __name__ == '__main__':
    test()
