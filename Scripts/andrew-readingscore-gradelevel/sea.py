import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from textwrap import wrap

data = pd.read_csv('data.csv')

# data['Dataset'] = ['\n'.join(wrap(x, 23)) for x in data['Dataset']]
sns.set_style('ticks')
sns.set_context('paper')
box_plot = sns.catplot(y = 'Dataset', x = 'Reading Ease', data = data, orient='h', kind='box', aspect = 4, height = 2, width = .3, palette = 'pastel', dodge = True)
plt.title('Comparison of Our Dataset to Other Media')

ax = box_plot.axes
lines = ax.get_lines()
categories = ax.get_xticks()

for cat in categories:
    # every 4th line at the interval of 6 is median line
    # 0 -> p25 1 -> p75 2 -> lower whisker 3 -> upper whisker 4 -> p50 5 -> upper extreme value
    y = round(lines[4+cat*6].get_ydata()[0],1) 

    ax.text(
        cat, 
        y, 
        f'{y}', 
        ha='center', 
        va='center', 
        fontweight='bold', 
        size=10,
        color='white',
        bbox=dict(facecolor='#445A64'))
plt.savefig('reading-ease.png', dpi=300, bbox_inches = 'tight')

