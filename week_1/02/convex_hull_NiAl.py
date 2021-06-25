import os
import requests

import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt

from pymatgen.ext.matproj import MPRester


def get_fractions(entries):
    '''
    Convert formulas into fraction of Al.
    
    Args:
        entries: list of responses queried using MPRester.
        
    Returns:
        A list of fraction of Al in the formula.
    '''
    fractions = []
    for e in entries:
        split = e['pretty_formula'].split('Ni')
        if split[1] == '':
            n_Ni = 1
        else:
            n_Ni = int(split[1])
            
        s2 = split[0].split('Al')
        if s2[1] == '':
            n_Al = 1
        else:
            n_Al = int(s2[1])
            
        fractions.append(n_Al / (n_Ni + n_Al))
    return fractions



def plot_convex_hull(api_key):
    '''
    Plot the convex hull for NiAl compounds.
    
    Args:
        api_key: string for the MAPI key.
    '''
    props = ['formation_energy_per_atom', 'pretty_formula', 'e_above_hull']
    with MPRester(api_key=api_key) as mpr:
        entries = mpr.query({'elements':['Al', 'Ni']}, props)
    # display(entries)

    # clean up the entries
    fracs = get_fractions(entries)
    inds = np.argsort(fracs)
    fracs = sorted(fracs)
    fracs.insert(0, 0)
    fracs.append(1)
    entries_sorted = [entries[i] for i in inds]
    entries_sorted.insert(0, {'formation_energy_per_atom':0.0, 'pretty_formula':'Ni', 'e_above_hull':0.0})
    entries_sorted.append({'formation_energy_per_atom':0.0, 'pretty_formula':'Al', 'e_above_hull':0.0})

    # calculate convex hull using SciPy
    points = []
    for i in range(len(fracs)):
        points.append([fracs[i], entries_sorted[i]['formation_energy_per_atom']])    
    points = np.array(points)
    hull = ConvexHull(points)

    # plotting
    plt.rcParams.update({'figure.figsize':(15,6),      # Increase figure size
                         'font.size':20,               # Increase font size
                         'mathtext.fontset':'cm',      # Change math font to Computer Modern
                         'mathtext.rm':'serif',        # Documentation recommended follow-up
                         'lines.linewidth':5,          # Thicker plot lines
                         'lines.markersize':12,        # Larger plot points
                         'axes.linewidth':2,           # Thicker axes lines (but not too thick)
                         'xtick.direction':'in',       # Change x-axis ticks to point in
                         'ytick.direction':'in',       # Ditto for y-axis ticks
                         'xtick.major.size':8,         # Make the x-ticks longer (our plot is larger!)
                         'xtick.major.width':2,        # Make the x-ticks wider
                         'ytick.major.size':8,         # Ditto for y-ticks
                         'ytick.major.width':2})       # Ditto for y-ticks})
    fig, ax = plt.subplots()
    ax.plot(points[:, 0], points[:, 1], 'd', ms=8, c='C1')

    for i, simplex in enumerate(hull.simplices):
        if i > 0:
            ax.plot(points[simplex, 0], points[simplex, 1], 'k', lw=3.5, alpha=0.6)

    for i, e in enumerate(entries_sorted):
        if e['e_above_hull'] < 0.01:
            ax.plot(points[i, 0], points[i, 1], 'o', c='C2')
            if points[i, 0] == 0.6:
                ax.text(points[i, 0] + 0.05, points[i, 1] - 0.01, e['pretty_formula'], va='center', ha='center', size=20)
            elif points[i, 0] == 4/7:
                ax.text(points[i, 0] + 0.04, points[i, 1] - 0.05, e['pretty_formula'], va='center', ha='center', size=20)
            else:
                ax.text(points[i, 0], points[i, 1] - 0.065, e['pretty_formula'], va='center', ha='center', size=20)

    ax.set_xlabel('Fraction of Al in Al$_{x}$Ni$_{1-x}$')
    ax.set_ylabel('Formation energy (eV/atom)')
    ax.set_xlim([-0.05, 1.05])
    ax.set_ylim([-0.8, 0])
    ax.set_xticks(np.linspace(0, 1, 11))
    plt.show()
    # fig.savefig('../week_1/02/convex_hull_NiAl.png', dpi=300, bbox_inches='tight')