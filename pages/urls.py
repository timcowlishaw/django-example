# This file will handle which urls in our app map to which views in our python code.
# We `include` it from the `urls.py` file in the `djangoexample` folder, so that
# Django knows that this is here.

# To get started, we need the help of a function from django itself, `path`, which
# allows us to define a path in the url (ie the bit after the first slash).
from django.urls import path

# We then make a list of 'url patterns' which define our urls. Django comes looking
# for this object when we include the file. We'll leave it empty for now as we
# don't yet have any views (the square brackets are used to make a list of things,
# in this case it has nothhng inside).
urlpatterns = []