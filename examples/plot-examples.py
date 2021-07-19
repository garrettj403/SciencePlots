"""Plot examples of SciencePlot styles."""

import numpy as np
import matplotlib.pyplot as plt


def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel='Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig1.pdf')
    fig.savefig('figures/fig1.jpg', dpi=300)

with plt.style.context(['science', 'ieee']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('figures/fig2a.pdf')
    fig.savefig('figures/fig2a.jpg', dpi=300)

with plt.style.context(['science', 'ieee', 'std-colors']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    # Note: $\mu$ doesn't work with Times font (used by ieee style)
    ax.set_ylabel(r'Current (\textmu A)')  
    fig.savefig('figures/fig2b.pdf')
    fig.savefig('figures/fig2b.jpg', dpi=300)

with plt.style.context(['science', 'nature']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig2c.pdf')
    fig.savefig('figures/fig2c.jpg', dpi=300)

with plt.style.context(['science', 'scatter']):
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.plot([-2, 2], [-2, 2], 'k--')
    ax.fill_between([-2, 2], [-2.2, 1.8], [-1.8, 2.2],
                    color='dodgerblue', alpha=0.2, lw=0)
    for i in range(7):
        x1 = np.random.normal(0, 0.5, 10)
        y1 = x1 + np.random.normal(0, 0.2, 10)
        ax.plot(x1, y1, label=r"$^\#${}".format(i+1))
    lgd = r"$\mathring{P}=\begin{cases}1&\text{if $\nu\geq0$}\\0&\text{if $\nu<0$}\end{cases}$"
    ax.legend(title=lgd, loc=2, ncol=2)
    xlbl = r"$\log_{10}\left(\frac{L_\mathrm{IR}}{\mathrm{L}_\odot}\right)$"
    ylbl = r"$\log_{10}\left(\frac{L_\circledast}{\mathrm{L}_\odot}\right)$"
    ax.set_xlabel(xlbl)
    ax.set_ylabel(ylbl)
    ax.set_xlim([-2, 2])
    ax.set_ylim([-2, 2])
    fig.savefig('figures/fig3.pdf')
    fig.savefig('figures/fig3.jpg', dpi=300)

with plt.style.context(['science', 'high-vis']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig4.pdf')
    fig.savefig('figures/fig4.jpg', dpi=300)

with plt.style.context(['dark_background', 'science', 'high-vis']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig5.pdf')
    fig.savefig('figures/fig5.jpg', dpi=300)

with plt.style.context(['science', 'notebook']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig10.pdf')
    fig.savefig('figures/fig10.jpg', dpi=300)

# Plot different color cycles

with plt.style.context(['science', 'bright']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig6.pdf')
    fig.savefig('figures/fig6.jpg', dpi=300)

with plt.style.context(['science', 'vibrant']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig7.pdf')
    fig.savefig('figures/fig7.jpg', dpi=300)

with plt.style.context(['science', 'muted']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100, 500]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig8.pdf')
    fig.savefig('figures/fig8.jpg', dpi=300)

with plt.style.context(['science', 'retro']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig9.pdf')
    fig.savefig('figures/fig9.jpg', dpi=300)

with plt.style.context(['science', 'grid']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig11.pdf')
    fig.savefig('figures/fig11.jpg', dpi=300)

with plt.style.context(['science', 'high-contrast']):
    fig, ax = plt.subplots()
    for p in [10, 20, 50]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig12.pdf')
    fig.savefig('figures/fig12.jpg', dpi=300)

with plt.style.context(['science', 'light']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig13.pdf')
    fig.savefig('figures/fig13.jpg', dpi=300)

# Note: You need to install the Noto Serif CJK Fonts before running 
# examples 14 and 15. See FAQ in README.

with plt.style.context(['science', 'no-latex', 'cjk-tc-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'電壓 (mV)')
    ax.set(ylabel=r'電流 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14a.jpg', dpi=300)

with plt.style.context(['science', 'no-latex', 'cjk-sc-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'电压 (mV)')
    ax.set(ylabel=r'电流 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14b.jpg', dpi=300)

with plt.style.context(['science', 'no-latex', 'cjk-jp-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'電圧 (mV)')
    ax.set(ylabel=r'電気 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14c.jpg', dpi=300)

with plt.style.context(['science', 'no-latex', 'cjk-kr-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'전압 (mV)')
    ax.set(ylabel=r'전류 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14d.jpg', dpi=300)

# import matplotlib
# matplotlib.use('pgf')  # stwich backend to pgf
# matplotlib.rcParams.update({
#     "pgf.preamble": [
#         "\\usepackage{fontspec}",
#         '\\usepackage{xeCJK}',
#         r'\setmainfont{Times New Roman}',  # EN fonts Romans
#         r'\setCJKmainfont{SimHei}',  # set CJK fonts as SimSun
#         r'\setCJKsansfont{SimHei}',
#         r'\newCJKfontfamily{\Song}{SimSun}',
#         ]
# })

# with plt.style.context(['science', 'cjk-tc-font']):
#     fig, ax = plt.subplots()
#     for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
#         ax.plot(x, model(x, p), label=p)
#     ax.legend(title='Order', fontsize=7)
#     ax.set(xlabel=r'電壓 (mV)') 
#     ax.set(ylabel=r'電流 ($\mu$A)')
#     ax.autoscale(tight=True)
#     fig.savefig('figures/fig15.pdf', backend='pgf')
