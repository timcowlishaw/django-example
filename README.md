# Django example project

## Introduction
This is an example [python](https://www.python.org/) and [django]https://www.djangoproject.com/) web application, following roughly the architecture of the [TNA Find Case Law](https://github.com/nationalarchives/ds-caselaw-public-ui) project.

Look at the git commit history to understand how it has been put together, I'll make sure each commit is a well-documented, discrete step of the process.

## Getting started

You'll need to have installed [Docker](https://www.docker.com/) on your machine to run this project. Everything else will be installed automatically (and you can see how by looking at the commit history on the repo).


## Directory of files
 * `.editorconfig`: This file configures our text editors (such as VSCode or Atom) to format the code in this repository automatically in a consistent manner, so that we're all working from the same settings, and we don't make commits that are full of formatting changes.
 * `.gitignore`: This file tells git to ignore certain files, such as our local editor configuration and various things that python adds, that aren't relevant to the project itself, so that they don't get committed. We've added settings here for VSCode, Python, Django and Mac OS.
 * `docker-compose.yml`: This file tells Docker how to *run* our project. It relies on the `Dockerfile` which builds the project before running.
 * `Dockerfile`: This file describes the specific steps Docker needs to take to build our project as a *docker image*, which is like a description of a little virtual computer with our project and everything it needs already installed.
 * `README.md`: This README. It's in Markdown format, which is a handy, simple way of producing formatted text.
 * `requirements.txt`: This file tells a python utility called `pip` what python libraries and packages we need in order to run our app, and what versions we want of them. These are then installed automatically when we build the app - you can see where this is done in the `Dockerfile`.