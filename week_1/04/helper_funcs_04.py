import os
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.artist import Artist

from sklearn.linear_model import LinearRegression



def animate_gd():
    data = np.load('../../assets/data/week_1/01/number_weight.npy')
    m = len(data)
    X = np.column_stack([np.ones(m), data[:, 0]])
    y = data[:, 1].reshape(-1, 1)
    theta = np.zeros((2, 1))
    alpha = 1e-5
    err = np.sum((X @ theta - y)**2) / (2*m)

    fig, ax = plt.subplots()
    ax.scatter(data[:, 0], data[:, 1])
    h, = ax.plot([], [], c='k', alpha=0.5)
    t = ax.text(0, 0, '')
    plt.tight_layout()
    plt.close()

    def init():
        h.set_data([], [])
        return h,

    def animate(i):
        global err, theta, X, y, ax, t
#         h.set_data(data[:, 0], X @ theta)
        h.set_data([1, 100], [2, 200])
        Artist.remove(t)
        t = ax.text(2, 100, s=f'error = {err:.3f}', fontsize=18, ha='left', bbox=dict(fc='1.0', ec='white'))

        theta = theta - alpha * (X.T @ (X @ theta - y))
        err = np.sum((X @ theta - y)**2) / (2*m)
        return h, t

    plt.rcParams.update({'animation.html': 'jshtml', 'figure.figsize':(6, 4)})
    anim = animation.FuncAnimation(fig, animate, init_func=init, frames=20, interval=500, repeat=False);
    return anim