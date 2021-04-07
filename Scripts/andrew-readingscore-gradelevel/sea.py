import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', 150)
scores = pd.read_csv('scores.csv')
x = scores['Grade Level']
y = scores['Reading Ease']
sns.set()
sns.scatterplot(x, y)
plt.title('Sample Title')
plt.savefig('seaborn.png', dpi=150)