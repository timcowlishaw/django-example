# Django example project

## Introduction
This is an example [python](https://www.python.org/) and [django](https://www.djangoproject.com/) web application, following roughly the architecture of the [TNA Find Case Law](https://github.com/nationalarchives/ds-caselaw-public-ui) project.

Look at the git commit history to understand how it has been put together, I'll make sure each commit is a well-documented, discrete step of the process.

## Getting started

You'll need to have installed [Docker](https://www.docker.com/) on your machine to run this project. Everything else will be installed automatically (and you can see how by looking at the commit history on this repository).


## Directory of files
 * `.editorconfig`: This file configures our text editors (such as VSCode or Atom) to format the code in this repository automatically in a consistent manner, so that we're all working from the same settings, and we don't make commits that are full of formatting changes.
 * `.gitignore`: This file tells git to ignore certain files, such as our local editor configuration and various things that python adds, that aren't relevant to the project itself, so that they don't get committed. We've added settings here for VSCode, Python, Django and Mac OS.
 * `docker-compose.yml`: This file tells Docker how to **run** our project. It relies on the `Dockerfile` which builds the project before running.
 * `Dockerfile`: This file describes the specific steps Docker needs to take to build our project as a **docker image**, which is like a description of a little virtual computer with our project and everything it needs already installed.
 * `README.md`: This README. It's in Markdown format, which is a handy, simple way of producing formatted text.
 * `requirements.txt`: This file tells a python utility called `pip` what python libraries and packages we need in order to run our app, and what versions we want of them. These are then installed automatically when we build the app - you can see where this is done in the `Dockerfile`.

 ## Glossary:
 * **Backend**: The part of a **web application** that runs on the server. It's basically a computer program that generates web pages on the fly and sends them to your browser.
 * **Commit**: A set of changes in a **git** **repository**. It's a point in history of your codebase, so it contains a set of things updated at that point, a link to the previous point in history (which the changes are based on), and a message to explain what the changes are and why they happend.
 * **Container**: A little virtual computer, provided by **Docker**, that runs inside another physical computer (like your own one). You can use them to run your programming project, so each one is kept seperate in its own environment, and doesn't clutter up your real machine. Each container runs a Docker **Image**.
 * **[Django](https://www.djangoproject.com/)**: Django is what's called a **web framework**, a bit of computer software that handles a lot of the difficult and boring bits of writing a **web application** for us, so that we can concentrate on the parts that make our own project special. It gives us tools for dealing with computer networks, generating pages from templates, talking to databases, etc. Django works with the **Python** programming language.
 * **[Docker](https://www.docker.com/)**: A computer program that allows you to run **containers**, little self-contained virtual computers that contain your projects.
 * **Directory**: A folder on a computer, whether it's your own one, a server, or a **Docker** **container**.
 * **Frontend**: The part of a **web application** that runs in the browser on your computer.
 * **[git](https://git-scm.com/)**: A computer program that provides a  **version control** system.
 * **[GitHub](https://github.com)**: A web service for storing and sharing your **git** **repositories**. If you're reading this, it's probably the site you're on right now!
 * **Image**: In the world of **Docker**, an **Image** is a description of a virtual computer and everything installed on it. You can create one out of your project, which includes everything it needs to be run, then use it to start up a **container**.
 * **Localhost**: A special address / name for 'this computer, which ever one you're on  right now when you type it'. You can use it in URLs to connect to your development environment, which is running on your own computer, through a **port**.
 * **Port**: A computer connected to a network has lots of 'ports', which are like virtual connections to other computers. When a computer's acting as a server (providing a service for another computer to access), it opens one of these ports, so that other computers can communicate through it. Each port has a number, and some have special meanings (the web, for instance, works typically on ports 80 and 443). You connect to a specific port on a computer by including a colon in its url, for example: "http://localhost:8000", which says connect to the computer called "**localhost**" on port 8000.
 * **[Python](https://www.python.org/)**: A programming language, which is useful for all sorts of things, including writing the **backend** of a **web application**.
 * **Repository**: A **directory** which is set up with **git** **version control**. It might be on your computer or a colleague's, on **GitHub**, or elsewhere
 * **Version control**: Time travel for your files and one of the best inventions ever. It lets you set 'checkpoints' (called '**commits**' on all the files in a **directory**, so that you can undo and redo changes, or see what has changed between two points. It also makes it easy to collaborate with others - you can easily merge in changes other people have made to the same project, so that you're not at risk of editing the same file at the same time and writing over each other's changes. In short, it's absolutely indespensible for programming projects when you're working in a team, and really really really useful even if you're working on your own. Like most of the world, this project uses a version control system called **git**.
 * **Web application**: you know, a website! The main other important thing to know about them is that they're made up of a **backend** and a **frontend**.