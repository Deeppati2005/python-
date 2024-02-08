import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "C:/Users/deepp/OneDrive/Desktop/PYTHON/dataset/python_csv.csv")
df.head()
print(df)
print(df.info())
df1 = df.groupby(by='DEPT').size().reset_index(name='no of emp')
print(df1)

# no of emp

plt.pie(df1['no of emp'], labels=df1['DEPT'], autopct='%.2f%%')
plt.show()


# using bar chart plot no of men and female emp

df2 = df.groupby(by='SEX').size().reset_index(name='no of emp')
print(df2)

plt.bar(df2['SEX'], df2['no of emp'])
plt.show()

# count no of employess whose exp is more than 10

df3 = df[df.EXPERIENCE > 10]
print(len(df3))
