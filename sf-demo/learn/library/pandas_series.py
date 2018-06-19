#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/19

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

s = pd.Series([1, 3, 4, np.nan, 56, 33])
print(s)

# 数据可视化
print()
data = pd.Series(np.random.randn(100), index=np.arange(100))
# 累加数据
data.cumsum()
print(data)
data.plot()
plt.show()
