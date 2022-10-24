# This file will handle which urls in our app map to which views in our python code.
# We `include` it from the `urls.py` file in the `djangoexample` folder, so that
# Django knows that this is here.

# To get started, we need the help of a function from django itself, `path`, which
# allows us to define a path in the url (ie the bit after the first slash).
from django.urls import path

# We also need to import the views we've written in views.py so that we can wire them up to urls:
# the "." (dot) here signifies that we're importing from a views module that's inside the same folder
# as we're in currently.
from .views import home

# We then make a list of 'url patterns' which define our urls. Django comes looking
# for this object when we include the file.
urlpatterns = [
    # We add a pattern which matches our homepage path.
    # The homepage has a blank path ("ie there's nothing after the "/" (slash), so
    # this pattern, with a blank path, matches the homepage, and renders our "home" view.
    path("", home, name="home"),
]