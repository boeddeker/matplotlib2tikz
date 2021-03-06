# -*- coding: utf-8 -*-
#
desc = 'Simple $\sin$ and $\cos$ plots with markers'
# phash = 'ff2c46a629564547'
phash = 'ff2c47a6a1564545'


def plot():
    from matplotlib import pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    with plt.style.context(('ggplot')):
        t = np.linspace(0, 2*np.pi, 101)
        s = np.sin(t)
        c = np.cos(t)
        ax.plot(t, s, 'ko-', mec='r', markevery=20)
        ax.plot(t, c, 'ks--', mec='r', markevery=20)
        ax.set_xlim(t[0], t[-1])
        ax.set_xlabel('t')
        ax.set_ylabel('y')
        ax.set_title('Simple plot')
        ax.grid(True)
    return fig
