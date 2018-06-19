#!/usr/bin/env python 
# -*- coding:utf-8 -*-

# Created by nijianfeng at 18/6/19

import pandas as pd
import numpy as np
import xlrd as xlsx
import matplotlib.pyplot as plt

dates = pd.date_range('20180601', periods=8)
print(pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['a', 'b', 'c', 'd']))

# 通过ndarray创建
print()
print(pd.DataFrame(np.arange(12).reshape(4, 3)))

# 通过字典创建
print()
df = pd.DataFrame({'column1': 1.,
                   'column2': pd.Timestamp('20180619'),
                   'column3': [1, 2, 3, 4],
                   'column4': pd.Categorical(['test1', 'test2', 'test3', 'test4']),
                   'column5': [np.nan, 3, np.nan, 6],
                   }, index=list('abcd'))
print(df)
print(df.dtypes)
print()
print(df.sort_values(by=['column3'], ascending=False))

# 取行&取列
print()
print(df['a':'c'])
print()
print(df.column1)
print()
print(df.loc[['a', 'c'], ['column1', 'column3']])
print()
print(df.iloc[0:3, 2:5])
print()
print(df[df.column3 > 2])

# 设置数值
df.loc['d', 'column3'] = 5
df.iloc[0, 0] = 11
print()
print(df)

# 处理NaN的值  'any'只要有一个是NaN就drop，'all'全部是NaN才drop
print()
print(df.dropna(axis=0, how='any'))
print()
print(df.isnull())
# 是否存在NaN，有则为True
print(np.any(df.isnull()))
# 是否全部为NaN，有则为True
print(np.all(df.column5.isnull()))

# 读取文件
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', 300)
df = pd.read_excel('../temp/data_frame.xlsx')
print()
print(df.head(8))

# 数据合并
df1 = pd.DataFrame(np.ones((6, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.ones((6, 4)) * 1, columns=['a', 'b', 'c', 'd'])

# ignore_index无视原index,重新编号 union all
print()
print(df1)
print(df2)
print(pd.concat([df1, df2], ignore_index=True))
# join
print()
print(df1)
print(df2)
print(df1.merge(df2, left_on='d', right_on='d', how='outer'))
# left|right join
print()
df3 = pd.DataFrame(np.ones((6, 4)) * 0, columns=['a', 'b', 'c', 'd'])
df3.iloc[1:4] = 1
print(df1)
print(df3)
print(df1.merge(df3, left_on='d', right_on='d', how='inner'))

# 数据可视化
x = np.linspace(-1, 1, 50)
y1 = 2 * x + 1
y2 = x ** 2 + 1
print()
plt.plot(x, y1)
plt.plot(x, y2)
plt.show()
