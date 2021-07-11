(h1:11:presentations)=
# Giving presentations

One of the final deliverables in this module is a presentation to showcase your research.
Throughout the course of graduate school, you will be giving research-related talks _all the time_.
Depending on the occasion and the audience, these talks will range in technicality and length.
You may want to choose something short and fun when speaking to non-technical audiences, while for a thesis defense you should be prepared to delve into the technical details for up to 3 hours. 😱

For this module, you will be giving a [**science slam**](https://en.wikipedia.org/wiki/Science_slam), which is presumably named after [poetry slams](https://en.wikipedia.org/wiki/Poetry_slam) (spoken word).
In the same vein, a science slam is a short oral presentation that is given to **non-expert audiences**, where the focus is on communicating your work in a way that generates excitement and impresses impact, even when the audience isn't too familiar with your field.
It attempts to engage broader audiences in science by breaking down some of the formality and jargon in research and is great practice for science communication!

Please be aware that when we say "non-experts," we don't [necessarily] mean a "non-technical audience without a science background."
All of us (interns and mentors!), for example, are "non-experts" in all but a few fields, but we are still considered a "technical audience" as we know a thing or two about science. 😜
We will be the primary audience for your presentation, so keep that in mind when preparing your content.
But when in doubt, error on the side of less technicality.

```{margin}
**Also keep in mind**

No one:

Literally nobody: 

_Not a single soul_:

Reviewer #2: I don't like your presentation because it is too entertaining.
```



## Example slam

There are many great examples of science slams on YouTube, but out of convenience more than anything else, here we've included a slam talk that Enze gave as part of his _remote summer research internship_ (hey, sound familiar? 😉) last year at [Lawrence Livermore National Laboratory](https://www.llnl.gov/) (LLNL).

<div align="center">
    <iframe width="500" height="350" src="https://www.youtube.com/embed/0VJRdJ6JF3o" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

Some things to take note of:

- Enze was limited to only three minutes and three technical slides!
Not a lot of room to squeeze content in.
- For the content that he did fit in, note that it was still technically rigorous (microstructure, density functional theory, thermodynamic model, etc.), but kept at a high level without going into the detailed methodology.
This is _expected_ and the focus is on crafting a cohesive narrative (but you still gotta pack some 🥩 in).
- Note the heavy use of figures and light use of text.
You should similarly use figures and animations to tell your story, with clarifying text when needed.
Note how on the second slide Enze took an existing figure he made and modified the axes labels to facilitate communication of the main idea.
- Similar to your situation, Enze had to make this presentation just four weeks into his ten-week summer internship.
And so you can see that while there were one or two preliminary results, a lot of time was spent on context, motivation, impact, and future directions of the work.
You can do the same in your slam.
- There were some "fun" icons, jokes, and personal quirks inserted into the presentation, even though the audience was current and retired LLNL staff scientists (read: much older folks than Enze).
You can add in your own personality flairs (if you want) as that's the whole purpose of slams!



<!-- ```{sidebar} Tips for effective presentations
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQ4HIOq1EvZ3UUxGYc4UgryLwcmvBArR44Z7_mBgRF1moP6MK8xdYSmpsm-Dq3oluI46nUZr0UAlk-R/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" height="300" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
``` -->



## Structure

Alright, so how might you structure your final slam presentation?
Let's set the following guidelines:
- **Timing**: 5-7 minutes.
We won't cut you off per se, but you should aim for this range in your rehearsals.
There are six of you and factoring in a few minutes for possible questions, transitions, and delays, this will help ensure the whole thing wraps up in under an hour.
- **Slides**: No more than 6 slides.
Understand we're limiting you to help with the time control and with focusing your narrative to the salient points.
If you use more slides than this, you will likely go over time or you will have rushed through the slides too quickly.
You can, like in Enze's slam presentation, have animations and multiple pieces of content on one slide.

As to the sequence of slides, here is one _suggestion_ that you may or may not wish to follow:
1. Title slide: Title of presentation, your affiliation, and one figure (that may or may not reappear later; in any case, you shouldn't spend time discussing the figure here).
1. Intro slide: What is the problem and why is it significant?
1. Data/Results slide: Some data visualization, statistical analysis, initial model performance, etc.
1. Results/Discussion slide: Screening results, materials selection, feature importance, etc.
1. Conclusion: Key takeaways, what did **you** learn, what's next, etc.
1. Floater slide to expand on any of the above content, if you need.

The above isn't to say cram all those things onto one slide, but rather to give ideas for what you might show, depending on what you did.
We trust that you all have enough experience to ultimately make the call on the content, sequencing, and style that works best for you and your work.
We will _not_ be asking you to submit your presentation files.



## Logistics

Here's the timeline this week with regards to your presentations:

**Today**: We are introducing presentations today because we want you to start thinking about them early.
Even if you have some more data to analyze, you should have most of the pieces in place and can start compiling them into your final narrative.
Often times, by thinking of how you want to present your research, you'll figure out what steps remain, what figures still need to be generated, etc.
We want to make sure you have plenty of time left to do this!

**Tomorrow**: We'll introduce {doc}`../12/pull_requests` for how you will submit your presentation information (due Wednesday).
You can continue to finalize your research and your presentation.

**Wednesday**: By the end of today, you should have your presentation _information_ submitted. 
The presentation itself you can and should still work on, and you don't have to submit that.

**Thursday**: In the morning scrum, we'll decide the speaking order. 😁
In the afternoon, we'll start the slam presentations on Zoom **at a unique Zoom link in the calendar event**.
**Please feel free to invite guests** to come see your (and others') work!
Family, friends, mentors, or anyone else you think is appropriate.



## Tools

For your presentation slides, you can use Microsoft PowerPoint, Apple Keynote, Google Slides, [Canva](https://www.canva.com/), or a software of your choice.
For any figures that you make, we suggest that the DPI (dots per inch) be _at least 300_, which is something you can set in matplotlib using [`fig.savefig('my_figure_name.png', dpi=300, bbox_inches='tight')`](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html).
If you use figures from other sources (not made by you), that's also fine, but _please cite it_.
Other tools and tips for styling your presentation are best found online.



```{admonition} Did you know?
:class: tip
[_Science_ magazine](https://science.sciencemag.org/), one of the top journals that covers all fields of science, sponsors an annual [Dance Your Ph.D. contest](https://www.sciencemag.org/projects/dance-your-phd), and it's pretty awesome.
```

