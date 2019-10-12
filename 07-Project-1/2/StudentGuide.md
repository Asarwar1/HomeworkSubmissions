## Unit 7.2 - Pulling and Merging with Git

### Overview

Today, students will study **pulling from GitHub**; **merging branches with Git**; and **distributed PR workflows**.

### Class Objectives

* Students will be able to **pull a branch from GitHub**.

* Students will be able to **merge branches with Git**.

* Students will be able to **open, review, and merge PRs with GitHub**.

- - -
### Activities Preview

* **Git and GitHub Demo Continued...**
* Files/Instructions: 

  * [README.md](Activities/02-Stu_Pull/README.md)—`pull` activity

  * [README.md](Activities/03-Evr_Merge/README.md)—`merge` activity

  * [README.md](Activities/04-Evr_Pull_Requests/README.md)—PR Workflow activity

  * A **branch** is a timeline: Its it's own independent Git history of work.

  * Is the files on `master` and `other_branch` are the same, after branching onto and committing to `other_branch`?

  * The end result of **merging** branches is a _single_ branch with all the changes that have been made on either of the branches that you merged.

  * How might you get changes made on `other_branch` into `master`.

  * We can compare every pair  of file's timelines between the two branches, and keep the one with the most recent updates.

  * To demonstrate this via a text file.

    * Create a new Git repo, and add a simple text file on `master`. Make a series of changes and commits.

    * Checkout a new branch, and change the text file on that branch. Make a different series of changes and commits.

    * Switch back to `master`, and use `git log` to view the commit history.

    * Then, switch to your development branch, and use `git log` to view the commit history.

    * Along the way, we would have to make sure that multiple had never tried to change the same thing all at once.

    * If you had, Git will ask which version "wins"—we'll practice **resolving conflicts** in the next session.

    * Otherwise, we can simply **fast-forward** the target branch by updating its history with all of the changes made to the files in _either_ branch.

    * To pull from GitHub to a branch that we're on, we checkout the branch and write: `git pull origin <branch name>`.

    * If you run: `git pull origin master` _while on_ `other_branch`, you will **merge the most recent version of** `master` **on GitHub into** `other_branch`.

* **Project Work**

- - -

### Copyright

Coding Boot Camp © 2019. All Rights Reserved.
