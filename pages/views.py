from django.shortcuts import render

# CHANGE: We want to import the list of fruit defined in our system from our models file, so that we can display it in
# our `fruit` page.
from .models import all_fruit

# Create your views here.

# CHANGE: Let's create a view for our homepage. This is a python _function_, a little block
# of code / behaviour that can be reused and called from elsewhere - so it starts with the `def`
# keyword, short for `define` Our function is called `home` (but we could have called it whatever we like), and it takes a single _argument_, like
# an option or parameter, that django will pass to it when a user requests the page.
# This argument represents details about the http request the user makes, and while we don't need to concern ourselves too much with it,
# we need it as we'll need to pass it back to django later.
def home(request):
    # CHANGE: Inside our function, we just want to tell django to repsond with the html template we've created. We can use the
    # `render` function that django helpfully imports for us above in order to do that - it takes the request we received earlier as
    # an argument, and the name of the template we want to render. - (django automatically looks in the 'templates' directory of the
    # current application for these). This creates a `response` object which we `return` to django,
    # showing that we've finished out work here, and Django can continue processing the request.
    return render(request, "home.html")

# CHANGE: Now we'll create a view that displays our fruit. This works much like the home view we created before, except we pass some extra data
# to our template that it can render, in this case our list of all fruit which we imported above:
def fruit_list(request):
    # You can see that we do this by passing a third argument to 'render', which is a *dictionary*
    # - it maps keys ('fruit') to values (the list of fruit we imported). This means that that list
    # will be availble in our template with the name 'fruit'. This dictionary is often referred to as
    # the "context" for the page.
    return render(request, "fruit_list.html", {"fruits": all_fruit})