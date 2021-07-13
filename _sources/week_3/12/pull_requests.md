(h1:12:pull_requests)=
# GitHub pull requests

In Module 1, you learned a little bit about GitHub and how it can be used to share code between developers and with the general public.
More specifically, you used the command-line interface (CLI) to clone repositories (repos) to your local computing environment.
In this lesson, we'll continue the discussion and explore two more features of GitHub: the **web user interface (UI)** and **pull requests (PRs)**.



## Web UI

Chances are, you have already seen the GitHub web UI if you've cloned a repo before, because that's where you will find the correct URL to clone.
As an example, [here is the repo for this textbook](https://github.com/enze-chen/mi-book).

As you can see, the UI is fairly clean with many symbols, lots of whitespace, and light colors.
This simplicity was [intentionally designed](https://github.blog/changelog/2020-06-23-design-updates-to-repositories-and-github-ui/) to better surface repo elements and key GitHub features.
Moreover, the developers of GitHub realized that in order to elevate GitHub to the next level and increase platform adoption, they had to start enabling more CLI features to be accessible through the UI.
This not only improves the user experience for everyone (who doesn't like point-and-click, drag-and-drop?), but also enables less programming-savvy users to collaborate on projects.

On the main page of this textbook's repo, you will notice that one of the most prominent features on the right-hand side is the **Contributors** list.
This panel lists everyone who has made at least one change to at least one file in this repo.
It is sensible for this to be featured since that is one of the purposes of using GitHub and credit should be given where credit is due.
However, you'll also notice that it's a little sad at the moment—Enze is the only contributor. 😢

But fear not!
As stated on the first day, _we are a team_, and a team functions best when everyone contributes, so **you will all soon become contributors** on this wonderful team project of ours. 😍



## Presentation abstract

<iframe src="https://docs.google.com/presentation/d/e/2PACX-1vQRf1t_lSmNrAxhnlQFDgN3hZUU9pnQX4B3Cn6guSBXhPEHasfAOi-F7QnuRFv8FKvB525dWd5EN70g/embed?start=false&loop=false&delayms=3000" frameborder="0" width="100%" height="480" allowfullscreen="true" mozallowfullscreen="true" webkitallowfullscreen="true"></iframe>



## Pull requests

In GitHub lingo, the phrase associated with a personal contribution to a project is a **pull request**, or PR.
When you "open a PR" or "submit a PR," what this means is that you made some changes to your personal version of a repo and you're ready to incorporate those changes into the main, public version of that repo.
The "pull" part of the name refers to the fact that the main project has to grab your changes, and the "request" part of the name refers to the fact that the maintainers of the project need to review and accept your changes before they can be incorporated (**merged** in GitHub lingo).

PRs are used _all the time_ on GitHub and in software engineering as it allows for individual contributions while maintaining certain consistency checks.
While we cannot _git_ into all the details at the moment 🤦‍, we hope you can at least appreciate why we're teaching you this concept and now we will put these ideas into practice.
Once you have made some changes, submitted a PR, and that PR gets approved, you will become a contributor on this project!



### Final presentation page

_In a different tab_, navigate to this page of the textbook: {doc}`../14/final_presentations`.
On that page, hover over Octocat and click {guilabel}`✏ suggest edit`.

```{image} ../../assets/fig/week_3/12/suggest_edit.png
:alt: suggest_edit
:align: center
:width: 100%
```



### Fork the repo

This will take you to a page in the web UI that looks like the following:

```{image} ../../assets/fig/week_3/12/github_fork.png
:alt: github_fork
:align: center
:width: 80%
```


Since you are not a maintainer for the repo (only Enze is), you have to make a copy of the files and can only edit those copies.
Making your personal copy of a repo is called a **fork** 🍴 in GitHub lingo, and you should click {guilabel}`Fork this repository`.
This should then take you to an interface that looks like the following:

```{image} ../../assets/fig/week_3/12/github_edits.png
:alt: github_edits
:align: center
:width: 100%
```



### Add your information

Now find your section on that page and add the information related to your presentation. 
If you don't have the information ready, no worries.
Cancel the changes for now (Enze will be periodically merging in others' changes) and you can always come back to it later by following the same steps.

```{attention}
To avoid this going, ha-ha, _terribly wrong_ (i.e., "merge conflicts" in GitHub lingo), please make sure you edit your section and your section **only**.
Please don't touch any other lines, including adding/removing spaces in others' sections!
```

For the emoji, title, and description, replace the entire `[your_XXX]` parts.
[Emojipedia](https://emojipedia.org/) is a good source for selecting cross-platform emojis.
For the image, change just `temp.png` to the name of your own figure file, with the extension.
Your figure name has to be unique to you, so we suggest something like `name_final.png` (e.g., `enze_final.png`), provided this is what you named the actual figure (PNG) file on your computer!
We'll upload this image to the repo shortly.



### Propose changes

```{image} ../../assets/fig/week_3/12/github_propose.png
:alt: github_propose
:align: center
:width: 100%
```

When you have completed your section, scroll to the bottom and create a short title for this set of edits that you made (see above).
When you are done, click {guilabel}`Propose changes` to take you to the next page where you can see the lines you've changed. 
Near the top, you should see a box that says something like {guilabel}`compare: patch-1`.
Make a note of the number.

```{image} ../../assets/fig/week_3/12/github_compare.png
:alt: github_compare
:align: center
:width: 100%
```



### Uploading your figure

Halfway there! 
You've updated your presentation details, which now references the figure you made, but that figure isn't in the repo yet!
Time to change that.

````{margin}
```{image} ../../assets/fig/week_3/12/github_forked.png
:alt: github_forked
:align: center
:width: 75%
```
````

First, navigate to your forked repo by clicking [Your avatar in the top-right corner] `>` {guilabel}`Your repositories` `>` **mi-book**, which should take you to a very similar page as the main repo, except the header has the image in the sidebar, saying "forked from enze-chen/mi-book."

````{margin}
```{image} ../../assets/fig/week_3/12/github_branch.png
:alt: github_branch
:align: center
:width: 90%
```
````

Next, find the dropdown that says {guilabel}`master ▾` and select the name associated with the change you made earlier, which should be `patch-1` or something similar.
As the surrounding text implies, these are different **branches** of your project, and this is an important feature when using git.
In essence, brances allow you to keep several different versions of your code (with say, different files edited/present in each one) so that different project members can independently work on different sections/features, and only merge them with the main branch (called `master`) when ready.
When you proposed changes with your presentation information, those changes were saved into the `patch-1` branch, and so you want to add your figure to that branch as well.
**Click the branch name** to switch you to that branch.

Next, navigate by clicking on the folders to `assets/fig/week_3/14` where you should only see `temp.svg`, `temp.png`, and maybe a few other figures, depending on how quickly Enze has merged other students' PRs.
Once here, click on {guilabel}`Add file` `>` {guilabel}`Upload files` and choose the image from your computer (make sure it matches the name you entered in `final_presentations.md`).
Then enter a descriptive title for this change and click {guilabel}`Commit changes` (commit directly to the `patch-1` branch).



### Finally, the PR!

```{image} ../../assets/fig/week_3/12/github_compare2.png
:alt: github_compare2
:align: center
:width: 100%
```

&nbsp; 

Almost there!
Now you should see a yellow banner at the top with a fat {guilabel}`Compare & pull request` button.
Click it!!

&nbsp; 

```{image} ../../assets/fig/week_3/12/github_open_pr.png
:alt: github_open_pr
:align: center
:width: 95%
```
This takes you to the PR dialogue, and you should note the following:

- Make sure that at the top, you are merging the correct source branch on the right-hand side (`your_username/mi-book:patch-1` or equivalent, _not_ `master`) to the correct destination branch on the left-hand side (`enze-chen/mi-book:master`, _not_ `gh-pages`).
- Write a descriptive title for your PR.
- Leave the box "Allow edits by maintainers" **checked** ☑.
- At the bottom, you can further verify that the "2 files changed" are `final_presentations.md` and `name_final.png`.

If everything looks good, you can click {guilabel}`Create pull request` and then ping Enze on Slack!
Woohoo! 🎉

-------- 

```{admonition} Submission deadline
:class: tip
A reminder that you should submit your PR **by 5:00PM PT Wednesday, 07/14**.
This gives us enough time to merge it in and fix things if something breaks.
```

### Wait, I made a mistake!

That's alright, just make the changes to your copy of the files/figures in your `patch-1` branch and submit another PR to `enze-chen/mi-book:master`.
That's the beauty of it. 🙂



