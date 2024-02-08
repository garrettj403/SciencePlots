"""Plot examples of SciencePlot styles."""

import numpy as np
import matplotlib.pyplot as plt
import scienceplots

import os

# Check we are in examples dir
current_dir = os.getcwd().lower()
if (current_dir.endswith('scienceplots')):
    os.chdir('./examples')
# Create 'figures' folder if it does not exist
if (not os.path.exists('./figures')):
    os.makedirs('figures')

def model(x, p):
    return x ** (2 * p + 1) / (1 + x ** (2 * p))


pparam = dict(xlabel='Voltage (mV)', ylabel=r'Current ($\mu$A)')

x = np.linspace(0.75, 1.25, 201)

with plt.style.context(['science']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig01a.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'no-latex']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig01b.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'ieee']):
    fig, ax = plt.subplots()
    for p in [10, 20, 40, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig02a.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'ieee', 'std-colors']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig02b.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'nature']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig02c.jpg', dpi=300)
    plt.close()

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
    fig.savefig('figures/fig03.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'high-vis']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig04.jpg', dpi=300)
    plt.close()

with plt.style.context(['dark_background', 'science', 'high-vis']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig05.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'notebook']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig10.jpg', dpi=300)
    plt.close()

# Plot different color cycles

with plt.style.context(['science', 'bright']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig06.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'vibrant']):
    fig, ax = plt.subplots()
    for p in [5, 10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig07.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'muted']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100, 500]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig08.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'retro']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig09.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'grid']):
    fig, ax = plt.subplots()
    for p in [10, 15, 20, 30, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig11.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'high-contrast']):
    fig, ax = plt.subplots()
    for p in [10, 20, 50]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order')
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig12.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'light']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.autoscale(tight=True)
    ax.set(**pparam)
    fig.savefig('figures/fig13.jpg', dpi=300)
    plt.close()

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
    plt.close()

with plt.style.context(['science', 'no-latex', 'cjk-sc-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'电压 (mV)')
    ax.set(ylabel=r'电流 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14b.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'no-latex', 'cjk-jp-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'電圧 (mV)')
    ax.set(ylabel=r'電気 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14c.jpg', dpi=300)
    plt.close()

with plt.style.context(['science', 'no-latex', 'cjk-kr-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title='Order', fontsize=7)
    ax.set(xlabel=r'전압 (mV)')
    ax.set(ylabel=r'전류 ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig14d.jpg', dpi=300)
    plt.close()

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
#     plt.close()

with plt.style.context(['science', 'russian-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title=r'Число', fontsize=7)
    ax.set(xlabel=r'Напряжение (mV)')
    ax.set(ylabel=r'Сила тока ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig16.jpg', dpi=300)
    plt.close()
    
with plt.style.context(['science', 'turkish-font']):
    fig, ax = plt.subplots()
    for p in [5, 7, 10, 15, 20, 30, 38, 50, 100]:
        ax.plot(x, model(x, p), label=p)
    ax.legend(title=r'Düzen', fontsize=7)
    ax.set(xlabel=r'Gerilim/Volt (mV)')
    ax.set(ylabel=r'Mevcut Güç/Akım ($\mu$A)')
    ax.autoscale(tight=True)
    fig.savefig('figures/fig17.jpg', dpi=300)
    plt.close()
