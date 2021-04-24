import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

data = pd.read_csv('data.csv')

sns.set_style('ticks')
sns.set_context('paper')
box_plot = sns.catplot(y = 'Dataset', x = 'Reading Ease', data = data, orient='h', kind='box', aspect = 4, height = 2, width = .3, palette = 'pastel', dodge = True)
plt.title('Comparison of Our Dataset to Other Media')


plt.savefig('reading-ease.png', dpi=300, bbox_inches = 'tight')

