import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

data = pd.read_csv('data.csv')

sns.set_style('ticks')
sns.set_context('paper')
flierprops = dict(markerfacecolor = '0.75', markersize = 2, linestyle = 'none')
box_plot = sns.catplot(y = 'Dataset', x = 'Grade Level', data = data, orient='h', kind='box', aspect = 4, height = 2, width = .3, palette = 'pastel', dodge = True, flierprops = flierprops)
plt.title('Comparison of Our Dataset to Other Media')


plt.savefig('grade-level.png', dpi=300, bbox_inches = 'tight')

