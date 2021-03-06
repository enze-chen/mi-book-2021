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

(h1:01:module)=
# Intro to Module 2


This segment is our "syllabus hour," which we have explicitly typed out below to avoid any confusion.
The three main sections are as follows:

1. {ref}`h2:01:structure`
1. {ref}`h2:01:resources`
1. {ref}`h2:01:community`


(h2:01:structure)=
## Structure and expectations

First, we'll start with a quick poll:
**Do you feel comfortable with being recorded on Zoom?**

<!-- <p align="center">
    <iframe src="https://app.sli.do/event/kgqntect/embed/polls/c6e8efef-64fb-4b44-86a5-9907761e3c79" width="300" height="360"></iframe>
</p> -->

The reason we ask this is because there will be a few sessions where some of us won't be able to make it, and we'd like to record those sessions so those folks can catch up on the information. 
But we also recognize some might feel uncomfortable about being recorded, so please let us know.
The recordings will **not** be shared with anyone outside of this group and will not be used for any other purposes (e.g., posted to YouTube, used for research).


### Schedule and timing ⌚

```{margin}
For a more detailed breakdown of each day, click the corresponding `Day XX` in the navigation bar on the left.
```

A condensed summary of everything in this module can be found at {doc}`../../preamble/schedule`.
We plan to hold interactive tutorials during the first week with live "lectures" and asynchronous "homework," for which we encourage you to work collaboratively and ask questions.
In the second and third weeks, you will be doing self-directed research and we will hold office hours (OH) and other special events.

In terms of timing, we'll kick off each day at 9:00 AM PDT and have an afternoon debrief at a time that we'll collectively decide right now. 
Note that we will **not** be following Berkeley Time in this module.
In terms of actual working hours, particularly during the self-directed research segment, understand that we're _very flexible_ in accomodating your personal schedules and work preferences, so just keep us updated.
There's also _no requirement or expectation_ to be working outside of "working hours," which we'll loosely say is 9-5 Mon-Fri.


### Assessments

To help build understanding and collect feedback, there will be a scaffolded sequence of assessments, which are a mix of reading, writing, coding, and making presentations.
These are (or at least, should be) individually low stakes and implemented with the following considerations in mind:

- You will **learn by doing**, which is particularly important when it comes to data science and programming.
- Much of the coding, even in self-_directed_ research, will be done in **groups**. 
Teamwork makes the dream work.
- The assessments **build on each other** so you can practice different ways of communicating science, culminating in a final presentation. 
- Consider these assessments to be **checkpoints** to gauge your learning and to help keep things moving during these short three weeks.
- There are **no grades** (obviously). The more effort you're able to put in, the more you will learn.
Thus, we hope you are excited to challenge yourself to learn new things in this module.


### Guest speakers

As mentioned in the kickoff meeting, one thing that we will try to incorporate into this module is inviting guest speakers to share their work and life story with us.
These are great career development opportunities for you to learn about the impact of materials informatics and how graduate school (or not!) can prepare you for this field.
We've tried to be very intentional about selecting speakers with diverse educational and professional journies for you to learn about (see their respective pages for more information and times).
**We kindly ask you to attend these talks and ask the speaker questions.**
They're all very enthusiastic to spend their time with us and they look forward to the discussions!


(h2:01:resources)=
## Resources and technical details

In order to successfully pull off a remote, data science research internship, we'll have to rely on quite a few different pieces of technology.
In this section, we'll be discussing how these pieces fit together to support your learning.

### Zoom

We will use Zoom for all of our synchronous meetings.
The link should've been sent to you in Slack and it can also be found in [this text file](https://drive.google.com/file/d/12Kk58b8DG8_QDMPbkUhnXA2NIAjfik47/view?usp=sharing).
We will use the same link for all events in this module (e.g., tutorials, OH, guest speakers, presentations).
Feel free to use the room at any time if you need to meet with someone (a peer or a mentor).

Since we're all pretty tired of Zoom meetings by now, please understand that we will be very intentional of when we are using Zoom.
We will try to maximize the amount of interaction and discussion to help all of us stay engaged with the material and for your questions to be answered. 
We invite you to actively participate during these live sessions, and we want to acknowledge that _participation can take several forms_:

- You can unmute and speak up.
- You can type in the chat.
- You can react with emojis and other [non-verbal feedback](https://support.zoom.us/hc/en-us/articles/115001286183-Nonverbal-feedback-and-meeting-reactions-).
- You can turn your video on.

Feel free to use the method(s) you're most comfortable with.


### Slack 

We will use Slack as our primary communication platform for sending private and group messages, in addition to files, images, and _emojis_. 🙌🥳😍🤍🐢
Let's keep our group conversations in the **#module-2 channel**.

We kindly ask that you are "active" during working hours on Slack.
We encourage you to [turn on notfications](https://slack.com/help/articles/201355156-Configure-your-Slack-notifications) during this time.
You can tag people with `@`, including individual (`@enze`) and multiple (`@channel`) users.
Outside of working hours though, please send notifications to others only if urgent.
Enze will pretty much respond to any message at any time within 15 minutes. 😛


### Jupyter Book

This curriculum/website is created using Jupyter Book, which is a project that facilitates the publication of professional, interactive websites that feature computational narratives.
We think it will greatly support your learning and we would like to point out a few features to aid your navigation and improve your experience.


#### Embedded content

By now, you've probably realized that the Jupyter Book interface is very simple, yet very powerful, with the ability to embed all sorts of content (e.g., Google Slides, Slido polls, images, links, YouTube videos).
This means we're able to keep all of the curriculum materials for this module in a centralized location, which hopefully makes it easier for you to keep track of everything. 
There's a handy search bar and navigation bar on the left-hand side for you to quickly locate content, and we encourage you to click around on your own time to familiarize yourself with the interface. 🙂
Please note that external links will open _in the same tab_, so you'll have to right-click or <kbd>Ctrl</kbd>+<kbd>Click</kbd> to open links in a new tab.


#### DataHub

We will be conducting tutorials in the [Python programming language](https://www.python.org/) and executing the Python code using interactive [Jupyter notebooks](https://jupyter.org/) {cite}`kluyver_2016`.
The principal reason we're using Jupyter Book for this curriculum is because this software allows us to directly compile Jupyter notebooks into this website while maintaining links back to the original notebooks.
We can then run the notebooks in the cloud without having to mess with individual installations of Python, which greatly increases accessibility.
To enable interactive code execution for these notebooks, which we will be doing throughout the tutorials, we can open the Jupyter notebook pages using the DataHub service generously provided by the [Division of Computing, Data Science, and Society](https://data.berkeley.edu/).
We will demonstrate how to use DataHub in the next lesson for today.


#### GitHub issues

We really want this textbook to be a living document that is continually refined, and one way to do so is to make the material open source on GitHub. 
This allows anyone to collaborate on this work, _including you all_.
If you spot an error (including typos!) or have suggestion for content, please don't hesitate to open an issue using the GitHub icon above.



(h2:01:community)=
## Our learning community 🌱

```{sidebar} Community norms (summarized)
<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vR4SoE0fc9-hcCoiUAOAaakzvdvIfLXbL3PXmaqaMMY3FfkiIcAbFJ0mb8kTpwN5j6HI-m7k53ppvei/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" height="300" align="right" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>
```

In the final section, we want to open up a discussion about some community norms for creating a positive and vibrant learning community.
We already have two listed, but would love to hear your thoughts during this quick brainstorm. 
We know it has been a very taxing year for everyone and want to make this space as welcoming and stress-free as possible.


### Active learning

Lectures are boring to listen to and they're boring to give, and overall not very effective for learning.
So, we'll be employing **active learning** strategies that will give you opportunities to discuss ideas, ask questions, test hypotheses, and take agency over your learning, which research has shown to be extremely important {cite}`freeman_2014`.
In addition to the more "obvious" activities like interactive coding and peer discussions, you'll also be providing feedback frequently---for us, for your peers, and for yourselves---as opportunities for reflection on growth.
Our hope is that you will feel comfortable participating in all of these activities (and don't find them _too_ tedious 😜) as we've tried to intentionally design them to maximize your learning.


### Trying new things

The pandemic has really forced all of us to change [several] gears in how we operate and how we think.
And while it has led to tremendous loss, it has also catalyzed change and opened new windows of opportunity.
In terms of higher education, our optimism leads us to ask the following: Rather than focusing on recreating what was lost, what _new pedagogy_ can we create?
This summer internship and using Jupyter Book to develop this module's curriculum are just two small examples of the new things your instructors are trying.

We also commend you for participating in this internship, as several of you noted that research is new for you.
That's awesome! 
And for those of you who have done research before: well, we're honored that you chose to come back and spend your summer with us.
Regardless of your previous experience, it's likely you will learn a lot of new concepts in this module, and we want to explicitly note that learning new things is _hard_. Like, really, _really_ hard.
As we mentioned in the kickoff meeting, we will likely fail when doing research, and _fail often_.

Fortunately, once we internalize these facts, it becomes not-too-hard to chart a path forward.
In fact, just as ML is able to learn from your failures {cite}`raccuglia_2016`, **you too will learn from your failures**.
We know that by signing up for this internship, you are all ready for this challenge and you all believe that ability can be developed (also known as a growth mindset {cite}`dweck_2016`).
With this mentality towards learning and the support of your peers and mentors, you'll surely fluorish in this module. 🌸


### We want to hear from you! 💬

Throughout this module, please do not hesitate to point out what's confusing or offer suggestions for improvement.
Tell us on Slack, on Zoom, or using the GitHub issues tracker.
This is the first time we're trying out this curriculum (sorry, 🐹) and your ideas can have a huge impact on future generations of students!




## References

```{bibliography}
:style: unsrt
:filter: docname in docnames
```

