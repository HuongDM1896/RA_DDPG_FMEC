import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

width = .4 # width of a bar
N = 4
ind = np.arange(N)

m1_t = pd.DataFrame({
 'Local IE' : [340.9244,322.3456,303.775, 304.1988 ],
 'Dedicated MEC' : [144.894, 120.974, 98.5154, 97.1278],
 'Greedy MECF' : [140.2746	,114.9506,	87.8138	,87.066],
 'Optimal MECF' : [134.7994, 105.8772, 82.355, 82.7788]})

m1_t[['Local IE', 'Dedicated MEC', 'Greedy MECF', 'Optimal MECF']].plot(kind='bar', figsize =(7, 5))

ax = plt.gca()
plt.xlim([-width, len(m1_t['Local IE'])-width])
plt.xticks(ind, ('RRA', 'URA', 'DDPG', 'DDPG - PER'))
plt.ylabel('Avg. Delay - Energy cost')
plt.show()