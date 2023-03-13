import pandas as pd
import numpy as np


def import_data_from_file():
    data = pd.read_csv('input.txt', sep=" ", header=None)

    matrix = np.array(data.iloc[:-2, :])
    a = np.array(data.iloc[-2, :])
    a = a[~np.isnan(a)]  # remove all nan values
    b = np.array(data.iloc[-1, :])
    b = b[~np.isnan(b)]
    return matrix, a, b
