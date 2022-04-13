from utils import bench
import tqdm
import numpy as np

import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
)

from tabox import SMA as this_SMA
from talib import SMA as that_SMA

@bench
def bench_this_sma():
    for i in range(100, 5000):
        for t in [2, 3, 5, 10, 30, 50]:
            close = np.random.random(i)
            this_ret = this_SMA(close, timeperiod=t)

@bench
def bench_that_sma():
    for i in range(100, 5000):
        for t in [2, 3, 5, 10, 30, 50]:
            close = np.random.random(i)
            that_ret = that_SMA(close, timeperiod=t)

if __name__ == '__main__':
    bench_this_sma()
    bench_that_sma()
