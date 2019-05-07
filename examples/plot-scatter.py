""" An example of a larger plot. """

import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use(['science', 'scatter'])

fig, ax = plt.subplots(figsize=(4,4))
ax.plot([-2, 2], [-2, 2], 'k--')
ax.fill_between([-2, 2], [-2.2, 1.8], [-1.8, 2.2], color='dodgerblue', alpha=0.2, lw=0)
for i in range(7):
    x = np.random.normal(0, 0.5, 10)
    y = x + np.random.normal(0, 0.2, 10)
    ax.plot(x, y, label=r"$^\#${}".format(i+1))
ax.legend(title='Sample', loc=2)
ax.set_xlabel(r"$\log_{10}\left(\frac{L_\mathrm{IR}}{\mathrm{L}_\odot}\right)$")
ax.set_ylabel(r"$\log_{10}\left(\frac{L_\mathrm{6.2}}{\mathrm{L}_\odot}\right)$")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
fig.savefig('figures/fig3.pdf')
fig.savefig('figures/fig3.jpg', dpi=300)
