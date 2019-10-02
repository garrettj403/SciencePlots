Science Plots
=============

*Format Matplotlib for scientific plotting* 

This repo has Matplotlib styles to format your plots for scientific papers, presentations and theses.

Installation
------------

Put all of the ``*.mplstyle`` files into your Matplotlib style directory. If you're not sure where this is, in an interactive python console type:

```python
import matplotlib
print(matplotlib.get_configdir())
```

You should get back something like ``/home/garrett/.matplotlib``. You would then put the ``*.mplstyle`` files in ``/home/garrett/.matplotlib/stylelib/`` (you may need to create the ``stylelib`` directory). If you're on macOS, you can run:

```bash
mkdir -p ~/.matplotlib/stylelib/
cp styles/*.mplstyle ~/.matplotlib/stylelib/
cp styles/misc/*.mplstyle ~/.matplotlib/stylelib/
cp styles/color/*.mplstyle ~/.matplotlib/stylelib/
```

Using the Styles
----------------

``science.mplstyle`` is the main style from this repo. Whenever you want to use it, simply add the following to the top of your python script:

```python
import matplotlib.pyplot as plt
 
plt.style.use('science')
```

You can also combine multiple styles together by:

```python
plt.style.use(['science','ieee'])
```

In this case, the ``ieee`` style will override some of the parameters from the main ``science`` style in order to configure the plot for IEEE papers (column width, fontsizes, etc.). 

To use any of the styles temporarily, you can use:

```python
with plt.style.context(['science', 'ieee']):
    plt.figure()
    plt.plot(x, y)
    plt.show()
```

Contribution
------------

Please feel free to add to this repo! For example, it would be good to add styles for different journals or perhaps new color cycles.

Examples
--------

The ``science`` style:

![alt text](examples/figures/fig1.jpg)

The ``science`` + ``high-vis`` styles:

![alt text](examples/figures/fig4.jpg)

The ``science`` + ``scatter`` styles:

![alt text](examples/figures/fig3.jpg)

You can also combine these styles with the other styles that come with Matplotlib. For example, the ``dark_background`` + ``science`` + ``high-vis`` styles:

![alt text](examples/figures/fig5.jpg)

**Note:** See the ``examples/`` directory for more!

Color Cycles
------------

The ``science`` + ``bright`` styles:

![alt text](examples/figures/fig6.jpg)

The ``science`` + ``vibrant`` styles:

![alt text](examples/figures/fig7.jpg)

The ``science`` + ``muted`` styles:

![alt text](examples/figures/fig8.jpg)

**Note:** The ``bright``, ``vibrant`` and ``muted`` styles are from Paul Tol's website (https://personal.sron.nl/~pault/). **They are color-blind safe.**
