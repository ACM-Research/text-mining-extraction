import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('crossData.csv')
sns.set_style('whitegrid')
sns.set_context('poster')
# sns.set(font='Gothic A1')
bar,ax = plt.subplots(figsize=(10,7))
ax = sns.barplot(x = 'Reading Ease', y = 'Economic Status', data = data, ci=None, palette='pastel',orient='h',dodge = True)
ax.set_title("Reading Ease and Economic Status")
plt.ylabel("")
# for rect in ax.patches:
#     ax.text(rect.get_width(), rect.get_y() + rect.get_height() / 2, round(rect.get_width(), 2), weight='bold', fontsize=13)

bar.savefig("econ.png", dpi = 150, bbox_inches = 'tight')





