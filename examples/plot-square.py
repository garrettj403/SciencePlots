""" An example of a larger plot. """

import numpy as np 
import matplotlib.pyplot as plt 

plt.style.use(['science'])

fig, ax = plt.subplots(figsize=(4,4))
ax.plot([-2, 2], [-2, 2], 'k--')
ax.fill_between([-2, 2], [-2.2, 1.8], [-1.8, 2.2], color='gray', alpha=0.2, lw=0)
for i in range(5):
    x = np.random.normal(0, 0.5, 20)
    y = x + np.random.normal(0, 0.2, 20)
    ax.plot(x, y, label=r"$^\#${}".format(i+1), marker='o', markersize=3, ls='')
ax.legend(title='Sample', loc=2)
ax.set_xlabel(r"$\log_{10}\left(\frac{L_\mathrm{IR}}{\mathrm{L}_\odot}\right)$")
ax.set_ylabel(r"$\log_{10}\left(\frac{L_\mathrm{6.2}}{\mathrm{L}_\odot}\right)$")
ax.set_xlim([-2, 2])
ax.set_ylim([-2, 2])
fig.savefig('figures/fig3.pdf')
fig.savefig('figures/fig3.pgf')
fig.savefig('figures/fig3.jpg', dpi=300)
