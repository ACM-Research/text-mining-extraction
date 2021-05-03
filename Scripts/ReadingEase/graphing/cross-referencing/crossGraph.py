import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('crossData.csv')

sns.set_style('whitegrid')
sns.set_context('paper')

bar,ax = plt.subplots(figsize=(10,6))
ax = sns.scatterplot(x = 'Reading Ease', y = 'Percent of Negative Statements', data = data, ci=None, palette='pastel')
ax.set_title("Reading Ease and Percent of Negative Statements in our Documents", fontsize=15)
bar.savefig("pctNegative.png", dpi = 300, bbox_inches = 'tight')





