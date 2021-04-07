import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows', 150)
scores = pd.read_csv('scores.csv')


plt.clf()
plt.figure(figsize=(12,8))
plt.scatter(scores['Grade Level'], scores['Reading Ease'])
plt.xlabel('Grade Level')
plt.ylabel('Reading Ease')
plt.title('Reading Ease over Grade Level')
plt.grid(True)

z = np.polyfit(scores['Grade Level'], scores['Reading Ease'], 1)
p = np.poly1d(z)
plt.plot(scores['Grade Level'],p(scores['Grade Level']), "r--")

plt.savefig('test.png',dpi=100)

# print(scores)