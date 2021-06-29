(h1:02:reading_docs)=
# Reading documentation

At this point, we've already introduced _a ton_ of concepts about Python and third-party Python packages (with more to come), so we want to give some pointers on how to search for and read documentation for Python code.
This way, you can get answers to your questions directly from the source and apply this knowledge to all of your future work.

````{sidebar} Wisdom of the Ancients
```{figure} ../../assets/fig/week_1/02/xkcd_wisdom.png
:align: center
:width: 100%
:alt: xkcd_wisdom
[xkcd comic 979](https://xkcd.com/979/).
```
````


## Searching for documentation

We've all been in situations in the past where some teacher mentions an off-hand comment like, "Oh, if you don't know what this is, just look it up on Google."
While we can appreciate the intent, this standalone comment can be potentially misguided as it's pretty daunting to sift through all the Google search results to find what [we may not even know] we need.
In a way, if we don't even know what something is, then by definition how would we know the proper keywords to conduct a search query?
And so we write these notes to provide some guidance on this matter.
Since we can't cover everything, we'll summarize two broad _categories_ of search queries that you might conduct for your work.


### Searching for an algorithm or use case

The first category is when you want to generally know the Python syntax for accomplishing a certain task.
Such as resolving an error message, as the figure suggests.
Your queries might look like the following:
```
how to create a NumPy array in Python
how to sort a list using lambda functions in Python
python IndexError: list index out of range
```

These queries are structured pretty much similarly to what you'd expect (i.e., what you would say if you were asking someone else).
For error messages, we recommend _copying the error message directly_ from your Jupyter notebook or terminal window output and throwing in "python."

You will then get a huge list of results to sift through, so we offer some guidance on what sources might be more helpful than others:

1. [Stack Overflow](https://stackoverflow.com/): Anything from the `stackoverflow.com` domain is a very good place to look for a solution. 
The solutions are contributed _and voted on_ by community members, and there's a standard of excellence for what makes a good answer (such as providing a _minimum working example_ for a solution).
1. Stack Overflow is part of the larger [Stack Exchange](https://stackexchange.com/) community, and you might find answers to more domain-specific questions (like [statistics](https://stats.stackexchange.com/)) on other sites (e.g., `stats.stackexchange.com`).
1. Any of the tutorial or blog sites will have plenty of code examples, and some particularly well-known ones are:
    - [Tutorials Point](https://www.tutorialspoint.com/index.htm): `tutorialspoint.com`
    - [GeeksforGeeks](https://www.geeksforgeeks.org/): `geeksforgeeks.org`
    - [W3Schools](https://www.w3schools.com/): `w3schools.com`
    - [Towards Data Science](https://towardsdatascience.com/): `towardsdatascience.com`
    - [KDnuggets](https://www.kdnuggets.com/): `kdnuggets.com`
    - [Analytics Vidhya](https://www.analyticsvidhya.com/blog/): `analyticsvidhya.com`
1. [YouTube](https://www.youtube.com/): Videos can be a great source for information as there seems to be a lot of different video tutorials out there now.
You may find it comforting to hear a human talk through your problems.
Or not. 😂
1. Source documentation will often have simple examples for you to learn from. More on this below.

Note that while we provide domains above for you to recognize the names, we still suggest _starting your search_ from a general search engine like Google and clicking the relevant results.
Hopefully, one of these sources will give you the exact usage pattern you were looking for, or something pretty close that you can adapt.



### Searching for a package/module/function

The second category is when you want to learn how a specific package works, like `pymatgen`, or the `MPRester` module, or `numpy.mean()`.
Yes, you are probably thinking of a specific use case, but maybe you're also just curious as to what the possibilities are, or the package isn't popular enough to have questions on a site like Stack Overflow.
For this, we suggest structuring your search query like:

```
pymatgen package documentation
MPRester pymatgen examples
numpy.mean function documentation
python requests package documentation
```

Notice that we try to be as **specific** as possible. 
If we want to look for documentation from the source, we include "documentation," and when we want to know usage examples/patterns, we explicitly include "examples."
If it's a package, we'll say that; and if it's a function, we'll say that too, and even write the search term that way ("numpy.mean").
If the package/function is a default one in Python, we recommend adding the keyword "python" as well.

While the previous websites will likely have answers for you, here we will suggest a different approach and that is to consult **the source documentation written by the package developers**.
The Python community prides itself on writing good documentation, and generally this is where you will find the most comprehensive and up-to-date information.
Moreover, Python documentation will have not only the syntax (e.g., function names, arguments, and return types) but **also examples** for how you can use those functions (more on this in {ref}`h2:02:reading_docs`).

So what are the source domains that you should look for?

1. If it's a general Python question, or a question about a package that comes bundled with Python (e.g., `os`, `json`), consult [the official documentation](https://docs.python.org/3/) at `docs.python.org/3/`.
1. If it's a third-party package, try to select links that are from the official documentation for that package.
The ones you'll likely come across in this module are:
- [NumPy](https://numpy.org/doc/stable/): `numpy.org/doc/stable/`
- [pandas](https://pandas.pydata.org/docs/): `pandas.pydata.org/docs/`
- [Matplotlib](https://matplotlib.org/stable/contents.html): `matplotlib.org/stable/contents/html`
- [Scikit-learn](https://scikit-learn.org/stable/index.html): `scikit-learn.org/stable/index.html`
- [Pymatgen](https://pymatgen.org/index.html): `pymatgen.org/index.html`
- [Matminer](https://hackingmaterials.lbl.gov/matminer/): `hackingmaterials.lbl.gov/matminer/`

We offer two more points of guidance regarding your search:
- You can _try using the search bar on these sites for direct results_, which are generally pretty good.
In other words, while we did not advise doing this in the previous section (since it's hard to pinpoint where we'll find answers to those broad inquiries), we _do_ recommend doing this if there's a question about how to use a specific package/function.
An example would be to actually click the NumPy link above and search `numpy.mean` directly on the search bar on that page.
- If you take the "Google search" route, be aware of _different versions_ of these packages, which may give different results.
You'll notice our links typed out above have the word `stable` in the URL, which is an alias for the most recent, stable version.
You might also run into `dev` (development) versions of the documentation (like NumPy v1.22) or need an older version (DataHub uses slightly older versions of these packages), and you can generally change this on the website itself.
Most of the time, _it doesn't make a difference_, but just be aware. 👀


(h2:02:reading_docs)=
## Reading the docs

Now that you've pulled up the documentation page, it still might not be very clear how to _read and interpret_ what's on this page.
Here, we hope to provide a breakdown of what each section is and what information to pay attention to, and we'll use the the documentation for the function [`numpy.mean()`](https://numpy.org/doc/stable/reference/generated/numpy.mean.html) as an example.
While your particular page will be different, the overall structure will be similar as [good] Python developers have all conformed to the same standard.

At the top of the page, there is the **function name** and the module(s) it lives under. 
This is followed by the **function header** which shows the input parameters.
All input parameters with an equal sign (`=`) are _optional_, with the value that follows being the default value.
Furthermore, _the order of the parameters is important_, because that determines how the values from the caller will be assigned if argument names aren't specified.
For example, if argument names are specified, we can specify them out of order:

```python
np.mean(a=arr, dtype=np.int32, axis=0)
```

But if argument names aren't specified, then the assignment is based on the order in the header:

```python
np.mean(arr, 1, np.float64)
```

where `a=arr`, `axis=1`, and `dtype=np.float64` is assumed.

Next we have a short **description** of what the function does, which in the example is `Compute the arithmetic mean along the specified axis.`

Then we have a verbose explanation of each input parameter, starting with the name **and type**.
When reading documentation, make sure to pay attention to the type that the function is expecting for maximum compatibility.
What follows is a description of what the parameter will do, and particular _special cases_ to be aware of.
Something that is nice about recent documentation is that it will note the version number that a particular parameter was introduced in, so you know what might be missing in older version of the package (for example, `where` is an invalid input argument in the DataHub version of NumPy, v1.19.5, since it was introduced in v1.20.0).

Next is the **return** value and type, along with a description.
Here the biggest thing to pay attention to is whether the output is returned as a **copy or in place**.

There are then a few notes for data type considerations, and sometimes links to related methods (like [`np.average()`](https://numpy.org/doc/stable/reference/generated/numpy.average.html) in the example), which can be particularly handy when you realized after reading the documentation that the function you actually want is a different one.

Finally, one of the most important things that you'll find at the end of NumPy, pandas, Matplotlib, and Scikit-learn documentation (among others) is a list of **examples** using that function and its various input arguments.
Studying these are often a great way to learn how the module/function behaves!


