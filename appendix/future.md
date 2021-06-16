---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(h1:appendix:future)=
# Future directions 🛣

````{margin} 
```{admonition} Contact
:class: tip

Enze can be reached at `chenze` at the Berkeley domain while Mark can be reached at `mdasta` at the same.
````

Here we will share bits and pieces of our vision for how interactive computing environments (such as the one demonstrated in this digital textbook, among others) can be extended to enhance materials science education more broadly.
If you have ideas or suggestions and would like to collaborate, please do not hesitate to contact us. 😍

```{note}
If you were looking for _content suggestions_ (i.e., what to study after going through this curriculum), please refer to {doc}`../week_3/15/next`
```



## Accessibility

Two of the main reasons we are such passionate educators because we strongly believe in the enabling potential of a quality education, and that education is _not_ a [zero-sum game](https://en.wikipedia.org/wiki/Zero-sum_game).
That's why in addition to interactivity, we designed for broad accessibility for everyone who wants to learn about MI, not just students at UC Berkeley.
We're proud to publicly share as much content as possible (under a [CC BY-SA License](http://creativecommons.org/licenses/by-sa/4.0/)) and we're grateful for the support from like-minded individuals (see {doc}`acknowl`).
We hope this makes it easier for others to adapt their own curriculum, or use pieces of this one verbatim, as they see fit.



## Scalability

What this speaks to is computing education at scale. 
MI makes it possible to bring computational thinking {cite}`wing_2006` to everyone.
The Jupyter Book organizes everything for easy access.

Larger programs?
More participation in MSE?
Such as [Code in Place](https://codeinplace.stanford.edu/course) that Enze section led for.
Can we do the same for MSE?
It remains an open question.
But if we don't at least try, how will we ever know?

TODO



## Integrate computing into other MSE courses

While it may seem obvious to include computational learning experiences into a module on MI, we believe computational materials science can be integrated more broadly across the entire MSE curriculum {cite}`enrique_2018`.
Enhance understanding by illuminating new pathways to understanding. 
Data analysis and visualization.

Broader reach, to engage more students, making CS _relevant_. 
We also need to understand the ethics of computing broadly in contexts beyond CS.



### Thermodynamics


```{sidebar} MP4 video
This video shows how the Gibbs free energy curves and their common tangent (top) can be used to construct the phase diagram (bottom). 
The points of tangency on the solid and liquid free energy curves mark the solidus and liquidus, respectively, in the phase diagram.
Animation made in Matplotlib {cite}`hunter_2007`.
<div align="center">
    <video width="100%" controls>
        <source src="../_static/phase_diagram.mp4" type="video/mp4" alt="test video">
    </video>
</div>
```

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Odio eu feugiat pretium nibh ipsum consequat. Non sodales neque sodales ut etiam sit amet nisl. Leo vel orci porta non pulvinar neque. Malesuada proin libero nunc consequat. Id volutpat lacus laoreet non curabitur gravida arcu ac. Ultrices tincidunt arcu non sodales neque sodales ut. Etiam non quam lacus suspendisse faucibus interdum posuere. Non arcu risus quis varius quam quisque id diam. Purus ut faucibus pulvinar elementum integer enim. Venenatis a condimentum vitae sapien. Luctus venenatis lectus magna fringilla urna. Egestas fringilla phasellus faucibus scelerisque eleifend donec pretium vulputate. Aliquet enim tortor at auctor urna nunc id cursus metus. Et ligula ullamcorper malesuada proin libero nunc. Suspendisse interdum consectetur libero id faucibus nisl. Feugiat nisl pretium fusce id.

Diam sit amet nisl suscipit adipiscing bibendum. Neque gravida in fermentum et sollicitudin. Ipsum nunc aliquet bibendum enim facilisis gravida neque. Justo eget magna fermentum iaculis eu non diam phasellus vestibulum. Nisi vitae suscipit tellus mauris. Adipiscing elit pellentesque habitant morbi. Viverra tellus in hac habitasse platea dictumst. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Pretium lectus quam id leo in vitae turpis massa sed. Laoreet non curabitur gravida arcu ac tortor dignissim convallis. Id venenatis a condimentum vitae sapien pellentesque habitant. Nec sagittis aliquam malesuada bibendum arcu. Eu lobortis elementum nibh tellus molestie nunc non blandit. Non blandit massa enim nec dui nunc mattis enim ut. Aliquet eget sit amet tellus cras adipiscing enim. Sollicitudin aliquam ultrices sagittis orci a. A lacus vestibulum sed arcu.

Arcu ac tortor dignissim convallis. Id venenatis a condimentum vitae sapien pellentesque habitant. Nec sagittis aliquam malesuada bibendum arcu. Eu lobortis elementum nibh tellus molestie nunc non blandit. Non blandit massa enim nec dui nunc mattis enim ut. Aliquet eget sit amet tellus cras adipiscing enim. Sollicitudin aliquam ultrices sagittis orci a. A lacus vestibulum sed arcu.



### Materials characterization

XRD is a great candidate for tabular data and scientific computing.
Module below used in Prof. [Andy Minor](https://mse.berkeley.edu/people_new/minor/)'s Materials Characterization course at UCB.
The widget is a little too much for [Thebe](https://thebe.readthedocs.io/en/latest/index.html) to handle, so a fully interactive version can be found on [Google Colaboratory](https://colab.research.google.com/github/enze-chen/learning_modules/blob/master/mse/XRD_trends.ipynb).


```{code-cell}
:tags: [remove-input,thebe-init]
### Python module imports
# General modules
import itertools

# Scientific computing modules
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
%matplotlib inline

# Interactivity modules
from IPython.display import HTML, display
from ipywidgets import interact_manual, interactive_output, fixed, \
                       IntSlider, FloatSlider, FloatLogSlider, RadioButtons, \
                       Button, Checkbox, Layout, GridspecLayout


def plot_XRD(a, wavelength, cell_type, thickness, T=0, label=True, K=0.94):
    """This function is called by the widget to perform the plotting based on inputs.
    
    Args:
        a (float): Lattice constant in nanometers.
        wavelength (float): X-ray wavelength in nanometers.
        cell_type (str): Crystal structure, can be FCC, BCC, or DC.
        thickness (float): Crystallite size in nanometers.
        T (int): Temperature in Kelvin. Default = 0.
        K (float): Scherrer equation parameter. Default = 0.94 (cubic).
        
    Returns:
        None, but a pyplot is displayed.
    """
    
    # Crystallographic planes
    planes = [[1,0,0], [1,1,0], [1,1,1], [2,0,0], [2,1,0], [2,1,1], [2,2,0],\
              [2,2,1], [3,0,0], [3,1,0], [3,1,1], [2,2,2], [3,2,0], [3,2,1]]
    planes_str = [f'$({p[0]}{p[1]}{p[2]})$' for p in planes]   # string labels

    # Set the basis
    basis = []
    if cell_type is 'FCC':
        basis = np.array([[0,0,0], [0.5,0.5,0], [0.5,0,0.5], [0,0.5,0.5]])
    elif cell_type is 'BCC':
        basis = np.array([[0,0,0], [0.5,0.5,0.5]])
    elif cell_type is 'DC':
        basis = np.array([[0,0,0], [0.5,0.5,0], [0.5,0,0.5], [0,0.5,0.5],
                          [0.25,0.25,0.25], [0.75,0.75,0.25], \
                          [0.75,0.25,0.75], [0.25,0.75,0.75]])
    else:
        raise ValueError('Cell type not yet supported.')

    # Convert planes to theta values (see equation above)
    s_vals = np.array([np.linalg.norm(p) for p in planes])
#     a += 1e-5 * T   # thermal expansion estimate; omit b/c a is alread indep var.
    theta = np.arcsin(np.divide(wavelength/2, np.divide(a, s_vals)))
    two_theta = 2 * np.degrees(theta)

    # Scherrer equation calculations
    beta = np.degrees(K * wavelength / thickness * np.divide(1, np.cos(theta)))
    sigma = beta / 2.355  # proportionality for Gaussian distribution

    # Structure-Temperature factor. Must... resist... for loops...
    s = np.sin(theta) / (10*wavelength)
    S = 2.210 * np.exp(-58.727*s**2) + 2.134 * np.exp(-13.553*s**2) + \
        1.689 * np.exp(-2.609*s**2) + 0.524 * np.exp(-0.339*s**2)
    f = 28 - 41.78214 * np.multiply(s**2, S)  # formula from Ch. 12 of De Graef
    F = np.multiply(f, np.sum(np.exp(2 * np.pi * 1j * \
                                     np.dot(np.array(planes), basis.T)), axis=1))

    # Multiplicity factor
    mult = [2**np.count_nonzero(p) * \
            len(set(itertools.permutations(p))) for p in planes]

    # Lorentz-Polarization factor
    Lp = np.divide(1 + np.cos(2 * theta)**2, 
                   np.multiply(np.sin(theta)**2, np.cos(theta)))

    # Final intensity
    I = np.multiply(np.absolute(F)**2, np.multiply(mult, Lp))
    
    # Plotting
    plt.rcParams.update({'figure.figsize':(10,5), 'font.size':22, 'axes.linewidth':2,
                         'mathtext.fontset':'cm'})
    xmin, xmax = (20, 160)
    x = np.linspace(xmin, xmax, int(10*(xmax-xmin)))
    fig, ax = plt.subplots()
    
    # Thermal effects. These functional dependencies ARE NOT REAL!!!
    thermal_diffuse = 3e1 * T * np.cbrt(x)   # background signal
    sigma += (T + 5) / 2000    # peak broadening from vibrations
    
    # Save all the curves, then take a max envelope
    all_curves = []
    for i in range(len(sigma)):
        y = stats.norm.pdf(x, two_theta[i], sigma[i])
        normed_curve = y / max(y) * I[i]
        # Don't include the curves that aren't selected by the Structure factor
        if max(normed_curve) > 1e1:
            max_ind = normed_curve.argmax()
            if label:
                ax.annotate(s=planes_str[i], \
                            xy=(x[max_ind], normed_curve[max_ind] + thermal_diffuse[max_ind]))
            all_curves.append(normed_curve)
    final_curve = np.max(all_curves, axis=0) + thermal_diffuse
    plt.plot(x, final_curve, c='C0', lw=4, alpha=0.7)

    # Some fine-tuned settings for visual appeal
    for side in ['top', 'right']:
        ax.spines[side].set_visible(False)
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(0, 1.05 * ax.get_ylim()[1])
    ax.tick_params(left=False, labelleft=False, direction='in', length=10, width=2)
    ax.set_xlabel(r'$2\theta$ (degree)')
    ax.set_ylabel('Intensity (a.u.)')
    plt.show()


# Now we create each slider individually for readability and customization.
a_widget = FloatSlider(value=0.352, min=0.31, max=0.4, step=0.001, 
                       description='Lattice constant (nm)', readout_format='.3f', 
                       style={'description_width':'150px'}, continuous_update=False,
                       layout=Layout(width='400px', height='30px'))

w_widget = FloatSlider(value=0.154, min=0.13, max=0.16, step=0.001, 
                       description='X-ray wavelength (nm)', readout_format='.3f', 
                       style={'description_width':'150px'}, continuous_update=False,
                       layout=Layout(width='400px', height='30px'))

t_widget = FloatLogSlider(value=10, base=10, min=0, max=3, step=0.1, 
                          description='Crystallite thickness (nm)',  readout_format='d', 
                          style={'description_width':'150px'}, continuous_update=False,
                          layout=Layout(width='400px', height='35px'))

T_widget = IntSlider(value=298, min=0, max=1000, step=1, 
                     description='Temperature (K)', readout_format='d', 
                     style={'description_width':'150px'}, continuous_update=False,
                     layout=Layout(width='400px', height='35px'))

c_widget = RadioButtons(options=['FCC', 'BCC', 'DC'], description='Crystal structure',
                        style={'description_width':'150px'}, continuous_update=False,
                        layout=Layout(width='350px', height='60px'))

l_widget = Checkbox(value=False, description='Annotate peaks?')

g = GridspecLayout(n_rows=4, n_columns=2, height='160px', width='820px')
g[0, 0] = a_widget
g[1, 0] = w_widget
g[2, 0] = t_widget
g[3, 0] = T_widget
g[0:2, 1] = c_widget
g[2, 1] = l_widget


out = interactive_output(plot_XRD, {'a':a_widget, 'wavelength':w_widget, 'cell_type':c_widget,
                                    'thickness':t_widget, 'T':T_widget, 'label':l_widget, 'K':fixed(0.94)})
display(g, out)
```

```{bibliography}
:style: unsrt
:filter: docname in docnames
```

