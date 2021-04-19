import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
df.head()
scores = df
print(scores)


sns.boxplot( y=df["Dataset"], x=df["Reading Ease"] );
plt.show()