# syntax=docker/dockerfile:1
# The above line tells your text editor that this is a Dockerfile, and it should
# highlight it as such, because it doesn't have  a file extension, so the editor
# wouldn't be able to tell otherwise.

# This file, along with docker-compose.yml, sets up Docker to run our project.
# This file describes the specific steps Docker needs to take to build our project
# as a *docker image*, which is like a description of a little virtual computer with
# our project and everything it needs already installed. By contrast, docker-compose.yml
# tells docker what to do with that image when we want to run it, for more details on that, go
# and have a look!

# First of all, we want to use an existing public Docker image
# which installs Python 3 as our base, this is what the FROM line does. It's
# usually the first thing in your Dockerfile.
FROM python:3

# Now we configure python with a couple of options that make it play a little more
# nicely with docker. This uses a mechanism called 'environment variables', indicated by the
# ENV command. These are like a dictionary of useful settings that anything running in your docker
# container can read.

#This first one ensures it doesn't write it's compiled code to disk and  clutter up our project:
ENV PYTHONDONTWRITEBYTECODE=1
# This one ensures that you can see any text it writes to the terminal immediately that
# it's written. Without it, it writes text to the display in 'chunks' and sometimes
# things like error messages don't appear immediately when the error happens. It's annoying.
ENV PYTHONUNBUFFERED=1

# Next we make a new directory inside the docker container where we will work.
# We call it "code" and put it at the top level of the container's filesystem.
WORKDIR /code

# Next we copy the file called `requirements.txt` from this directory into our new
# /code directory on the container. This file is where we keep a list of all the python
# libraries we're using (our 'dependencies' or 'requirements'), so that we can make sure
# they're installed automatically, and the right versions are used.
COPY requirements.txt /code/

# Now we've copied this, we'll ask the python package manager (called 'pip') to install
# all the dependencies in our requirements file for us. We already have this 'pip' command
# as it was installed by the base `python:3` image we declared at the top of this file.
RUN pip install -r requirements.txt

# Now let's copy all the rest of our project (everything in this folder) over into the
# /code directory on the container.
COPY . /code/

