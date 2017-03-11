import numpy as np
import pandas as pd


def is_type(df, baseType):
    test = [issubclass(np.dtype(d).type, baseType) for d in df.dtypes]
    return pd.DataFrame(data=test, index=df.columns, columns=["test"])


def is_float(df):
    return is_type(df, np.float)


def is_number(df):
    return is_type(df, np.number)


def is_integer(df):
    return is_type(df, np.integer)


def calc_entropy(df, var, wgt=None):
    tmpdf = df.copy()
