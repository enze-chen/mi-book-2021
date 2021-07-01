import os
import json

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.artist import Artist

from sklearn.linear_model import LinearRegression, Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.model_selection import KFold, cross_val_score, cross_val_predict



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



def gen_data(arr):
    rng = np.random.default_rng(seed=2)
    n = 10

    X = np.reshape(rng.choice(arr, size=n, replace=False), (-1, 1))
    y = X ** 2 + 2 * np.reshape(rng.normal(size=n), (-1, 1))

    X2 = rng.choice(arr, size=3, replace=False)
    y2 = X2 ** 2 + 2 * np.reshape(rng.normal(size=3), (-1, 1))

    return X, y, X2, y2



def ml_fitting(d, dom, X1, y1, X2, y2):
    lr = LinearRegression()
    kfold = KFold(n_splits=5, shuffle=False)
    featurizer = PolynomialFeatures(d)
    Xp = featurizer.fit_transform(X1)
    lr.fit(Xp, y1)

    domp = featurizer.fit_transform(dom)
    yp = lr.predict(domp)

    yhat = lr.predict(Xp)
    train_err = mean_squared_error(y1, yhat, squared=False)

    y2hat = lr.predict(featurizer.fit_transform(X2))
    val_err = mean_squared_error(y2, y2hat, squared=False)


    return yp, train_err, val_err



def plot_styling(ax, degree):
    ax[0].set_xlim(0, 6)
    ax[0].set_ylim(-5, 35)
    ax[0].set_xlabel('$x$')
    ax[0].set_ylabel('$y$')
    ax[0].legend(frameon=False)
    ax[1].set_xlabel('degree of polynomial (complexity)')
    ax[1].set_ylabel('error')
    ax[1].set_xlim(1, degree-1)
    ax[1].legend(frameon=False)
    plt.show()

















