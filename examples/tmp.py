""" An example of the 'science' theme. """

import numpy as np 
import matplotlib.pyplot as plt 

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))

x = np.linspace(0.75, 1.25, 201)
# with plt.style.context(['sciencem):
    # x = np.linspace(0.75, 1.25, 201)
    # fig, ax = plt.subplots()
    # for p in [5, 7, 10, 15, 20, 30, 38, 50, 100, 500]:
    #     ax.plot(x, model(x, p), label=p)
    # ax.legend(title='Order', fontsize=7)
    # ax.set(xlabel='Voltage (mV)')
    # ax.set(ylabel='Current ($\mu$A)')
    # ax.autoscale(tight=True)
    # fig.savefig('figures/fig8.pdf')
    # fig.savefig('figures/fig8.jpg', dpi=300)

plt.figure()
plt.plot(x, model(x, 5),  c='#4165c0')
plt.plot(x, model(x, 7),  c='#e770a2')
plt.plot(x, model(x, 10), c='c')
plt.plot(x, model(x, 15), c='darkgrey')
plt.plot(x, model(x, 20), c='#f79a1e')
plt.plot(x, model(x, 30), c='#ba7dcd')
# plt.plot(x, model(x, 38))
plt.show()