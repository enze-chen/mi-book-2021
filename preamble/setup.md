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

(h1:pre:setup)=
# Setup


```{important}
**Estimated time: 15-30 minutes**. 
We greatly appreciate you taking the time to complete these tasks _before_ the first day we meet (Monday, June 28th). 🙇‍♂️
If you have any questions or encounter difficulties, please don't hesitate to ping us! 
```



## Sign up for accounts

Thanks to the great minds behind [Project Jupyter](https://jupyter.org/), many of whom are here at UCB(!), we don't have to worry about installing any additional software on our personal computers.
However, in order to take full advantage of all of the interactive features in this curriculum, we do ask that you sign up for online accounts on the following platforms.
We will provide detailed instructions with screenshots in each section to help guide you.

```{note}
The objective here is have these accounts *created and ready for use*; we'll provide more details on how we expect you to use these features later on at the appropriate times.
```

```{note}
If you already have a GitHub, Hypothesis, and/or Materials Project account, you do _not_ have to create a new account and should just use your existing one on that platform.
```



### GitHub

[GitHub](https://github.com/) is a platform where people can store the code they write inside _repositories_ that can then be shared with the public.
There are many good reasons for sharing code, including starting collaborations, showcasing your skills, broadening your impact, etc.
This textbook, for example, is hosted on GitHub! 😉

GitHub is loaded with cool features, and in this module, we will expose a few of those in the web user interface (UI). 
Therefore, we ask that you sign up for a GitHub account by going to: https://github.com/join, which will take you to a page that looks like:

```{image} ../assets/fig/preamble/github_join.png
:alt: github_join
:align: center
:width: 66%
```    
&nbsp;   

Enter a username, email, and password that you can remember.
You can probably uncheck the "Email preferences" box.
Verify that you're a human and then click {guilabel}`Create account`.
You will have to also verify your email and go through a few more steps to set up your account (you can skip the personalization steps).


#### Test GitHub account

You may recall from your previous classes or just common sense that it's a good idea to _conduct tests_ to make sure that your software (or in this case, our account) is behaving as expected.
Hover over the [Octocat](https://github.com/octocat) button (the GitHub logo) in the top-right corner of this page and click "💡`open issue`."
If it successfully opens an issue for you, then your account is all set up and you can move on.
There's no need to submit the issue (you can just close the tab), unless you actually have an issue.



### Hypothesis

[Hypothesis](https://web.hypothes.is/) is a neat little tool that we'll be testing out to facilitate questions and discussions in context.
It allows you to **highlight and annotate directly on this webpage** and the changes _will remain_ even if you close the browser.
It will be our first time using this tool, and we hope it helps encourage participation and allows you to ask very targeted questions.

1\) To sign up for a Hypothesis account, please go to: https://hypothes.is/signup, which will take you to a page that looks like:

```{image} ../assets/fig/preamble/hypothesis_signup.png
:alt: hypothesis_signup
:align: center
:width: 55%
```    
&nbsp;   

Enter a username, email, and password that you can remember.
Check the first box, [probably] don't check the second box, and then click {guilabel}`Sign up`.

2\) Then, _using your UCB account_, open [this Google Drive file](https://drive.google.com/file/d/12Kk58b8DG8_QDMPbkUhnXA2NIAjfik47/view?usp=sharing) and find the link for our private Hypothesis user group that you should join. 
This will keep our comments a little more private and makes it easier for us to search for each other's comments (the public Hypothesis has over 1.5 million comments, lol).

#### Test Hypothesis account

To test your Hypothesis account, add your response to the comment Enze left on the following question: Should Oski learn materials science?
In order to see my comment, you will have to open up the Hypothesis tab on the page ({guilabel}`<` in the top-right corner) and change the user group to {guilabel}`MSD internship 2021`.

````{panels}
1\. Open Hypothesis by clicking {guilabel}`<`
^^^
```{image} ../assets/fig/preamble/hypothesis_1.png
:alt: hypothesis_1
:height: 150px
:align: center
```

---

2\. Change group to {guilabel}`MSD internship 2021`
^^^
```{image} ../assets/fig/preamble/hypothesis_2.png
:alt: hypothesis_2
:height: 150px
:align: center
```
````
&nbsp;   

Now you should see the question above highlighted (in blue, on my computer) and my comment appear in the Hypothesis sidebar.
Please contribute your thoughts too. 🙂
You will also be able to _add your own annotations anywhere in this book_ and it will only be viewable by members of our user group.



### JupyterHub/DataHub

```{code-cell}
:tags: [remove-cell]
hidden_message = 'You will never see this.'
```

If you've taken a class like DATA 8 or DATA 100 at UCB (among others), you will already be familiar with DataHub.
This platform allows us to run Python code stored inside Jupyter notebooks in the cloud without having to mess with local installations of Python. 
Moreover, you will each get individual copies of all of the files in this repo and any changes you make to those files will be saved to your personal DataHub account!
\#bless 

#### Test DataHub account

To verify that you can access UCB's DataHub for the interactive exercises, hover over the {fa}`rocket` icon in the top-right corner and click {guilabel}`JupyterHub`.
You should be taken to a CalNet login page, whereupon after you enter your login credentials, you should see DataHub start to boot up.
Make sure this completes, and when it does, you can close the tab as you should be all set.

```{note}
You have to enter DataHub through this textbook (at least once, and anytime we update the notebooks) in order for these files to sync with your personal DataHub repo.
```



### Materials Project

A lot of the data that we will analyze in this module come from the [Materials Project](https://materialsproject.org/) (MP) database, which is an initiative spearheaded by some fine folks at UCB and LBL (Mark is a co-PI, or co-principal investigator, for MP). 
Naturally, in order to access this data, you will have to create an account, which you can conveniently do with your UCB Google account (Enze does this for his research).

Please go to this link: https://materialsproject.org/janrain/loginpage/, and click {guilabel}`Sign in with Google`.
Follow the steps to completion.

#### Test MP account

After you finish authenticating, see if you can click {guilabel}`Dashboard` in the menu bar, which takes you to a page that looks like: 

```{image} ../assets/fig/preamble/mp_dashboard.png
:alt: mp_dashboard
:align: center
:width: 100%
```    
&nbsp;   

You should see your `API key` in the place where Enze drew the black line.
Do **not** share this API key with anyone as it is unique to you.
More on this in the near future.



## Update software

To ensure the smoothest user experience possible, we kindly also ask you to update the software on your computer. 
You only have to do this once before the module begins.


### Zoom

We will be using Zoom for all of our synchronous meetings this summer and you should have received information already for which Zoom link to use.
To take advantage of all of the latest enhancements (like _all_ emojis!) and security features, **please update your Zoom client** to the latest version.
We recommend using the desktop client (it's highly likely you're already using this) and it should be as simple as clicking your profile picture in the top-right corner and the clicking {guilabel}`Check for Updates` (see image below).
More information can be found in their [support documentation](https://support.zoom.us/hc/en-us/articles/201362233-Upgrade-update-to-the-latest-version).

```{image} ../assets/fig/preamble/zoom_update.png
:alt: zoom_update
:align: center
:width: 85%
``` 


### Slack

We will be using [Slack](https://slack.com/) for communications this summer, and we hope that you all feel comfortable reaching out to us (instructors) and each other on Slack with any questions.
You should already have an account on our Slack workspace, and it doesn't really matter to us whether you use the browser version of Slack or the desktop app, as long as you're monitoring it for updates during working hours (you can set notifications in Preferences; see left panel below).
If you do choose the desktop app, make sure you also understand how to update it (see right panel below).
The Slack channels you should join are 

- `TODO`, `TODO`, ...    

and we will discuss more details during our first meeting.

````{panels}
Change Slack settings (e.g., notifications)
^^^
```{image} ../assets/fig/preamble/slack_pref.png
:alt: slack_pref
:width: 100%
:align: center
```

---

Update Slack (desktop app only)
^^^
```{image} ../assets/fig/preamble/slack_update.png
:alt: slack_update
:width: 100%
:align: center
```
````



### Web browser

Most of this curriculum should be fully functional in any modern web browser, though we find that the experience seems to work best on [Google Chrome](https://www.google.com/chrome/), so we'll "recommend" that.
[Firefox](https://www.mozilla.org/en-US/firefox/new/) should also be fine, but Safari and Edge may have a few hiccups.
Regardless of which browser you use, we ask that you **please update it** at the start of this module since we will be relying heavily on the browser for our curricular activities.
All browsers appear to have adopted a similar structure of checking for updates using `[Menu] > Help > About` (see images for examples), while Safari can be updated through the App Store.

````{panels}
Update Chrome
^^^
```{image} ../assets/fig/preamble/chrome_update.png
:alt: chrome_update
:width: 100%
:align: center
```

---

Update Firefox
^^^
```{image} ../assets/fig/preamble/firefox_update.png
:alt: firefox_update
:width: 100%
:align: center
````



### Slido poll

For quick check-ins and formative assessments, we'll be using [Slido polls](https://www.sli.do/) throughout this curriculum.
In order for this to work, you will have to **enable [third-party] cookies** in your browser, so please make sure this setting is enabled.
If so, you should be able to submit a vote in the test poll below.
If not, please look up how to enable cookies for your browser. 🍪

<p align="center">
    <iframe src="https://app.sli.do/event/yv5xrtyg/embed/polls/49113d57-715d-48ea-90bd-78e44f336f29" width="300" height="300"></iframe>
</p>


