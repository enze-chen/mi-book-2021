(h1:02:databases)=
# Databases

Up until now, we've focused a lot on files and how different file types are suitable for different kinds of materials data and informatics applications.
For an individual user working in a particular domain, files are familiar and friendly to work with and simply make the most sense.
But in addition to files, another common source for data is a **database**, which consists of structured information that is controlled by a management system.
Given the rapid development of several materials-related databases and your potential need to pull data from these sources, we'll spend some time in this lesson discussing their purpose and usage, with a particular focus on a local product: [The Materials Project](https://materialsproject.org/).



## Why might we use a database?

It is likely that many of you have never used a database before (that's OK!), so let's start by discussing why a database is even necessary.
When we talk about structured data in databases, what you should picture in your head is _not_ something like Google Drive that stores a collection of files, but rather a platform that stores a collection of _pandas DataFrame-esque objects_ (the actual DataFrames, not CSV files of that data).
This is a crude analogy, but one that relates databases to something you already have experience with.
And just as how you found DataFrames easy to work with thanks to its **indexing** capabilities, databases too are indexed in a way that facilitates data retrieval (we call these _queries_), slicing, and more.
The other details can be saved for a dedicated course like [CS W186](https://www2.eecs.berkeley.edu/Courses/CSW186/), but some general reasons for using a database include:

- When you have _too much data_ to sensibly organize into files.
Besides, we saw that all files had limitations in their expressiveness, and we can't just store everything in binary files because then we have no idea what's in it until it's opened by the appropriate software.
- When you need to **scale up** your operations to many users accessing multiple pieces of data _concurrently_.
- You need a _standardized, flexible, and fast data access pattern_ that doesn't just involve combing through files.
Particularly if the data are spread into bits and pieces across many different "files" uploaded to the database at different times, by different users, etc.
- You need to enforce permissions and other security protocols that goes beyond "who has access to which files."



## What materials-related databases are publicly accessible?

Here is a list of some common materials databases (and data infrastructure, more broadly) that you might consult for self-directed research:

- [AFLOW](http://aflowlib.org/): First-principles calculated properties mostly for inorganic crystal structures.
- [Crystallography Open Database](http://nanocrystallography.org/): Crystal structures of organic, inorganic, and metal-organic compounds.
- [Materials Data Facility (MDF)](https://www.materialsdatafacility.org/): Data publication platform for materials datasets.
- [Open Quantum Materials Database (OQMD)](http://oqmd.org/): First-principles calculated properties mostly for inorganic crystal structures.
- [Materials Project (MP)](https://materialsproject.org/): First-principles calculated properties similar to AFLOW and OQMD.
- [Citrination](https://citrination.com/): A database of various materials data contributed by the MI community.
- [MatWeb](http://matweb.com/): A database for properties of various engineering materials and their datasheets.
- These aren't databases _per se_, but there are other websites with lots of materials-related data such as Wikipedia, WolframAlpha, etc.

For more sources, you can try searching on Google, reading MI review papers such as the one by [Himanen et al. _Adv. Sci._, 2019](https://onlinelibrary.wiley.com/doi/abs/10.1002/advs.201900808) {cite}`himanen_2019`, or looking at the "Data availability" sections at the end of relevant papers.



## The Materials Project

We'll begin our discussion of the Materials Project with these slides:

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQbK8wWVG8nuv3gNYzLP_ajJye7onF3FIpn89gUEruHwh5E2L3WrzJpufM3T47cMXsLgFHD3xfVuV9o/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" height="480" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>



### Exploring the UI

This will be done as part of the above discussion.



### Exploring the API

Please see the accompanying Jupyter notebook.



## References

Here are some more papers if you're interested in the technical details behind the Materials Project {cite}`jain_2013, ong_2013, ong_2015`.

```{bibliography}
:style: unsrt
:filter: docname in docnames
```

