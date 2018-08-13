""" An example of the 'science' + 'subfigure' themes. """

import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use(['science', 'subfigure'])

x = np.linspace(0.75, 1.25, 201)

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

fig, ax = plt.subplots()
for p in [10, 15, 20, 30, 50, 100]:
    ax.plot(x, model(x, p), label=p)
ax.legend(title=r'Order')
ax.set(xlabel=r'$V_0 / V_\mathrm{{gap}}$')
ax.set(ylabel=r'$I_\mathrm{{dc}}^0 / I_\mathrm{{gap}}$')
ax.autoscale(tight=True)
fig.savefig('figures/fig2.pdf')
fig.savefig('figures/fig2.pgf')
fig.savefig('figures/fig2.jpg', dpi=300)
