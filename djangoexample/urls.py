"""djangoexample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# CHANGE: In order to wire up the URLS for our new application, we need the help
# of another function defined in django itself - `include`, which allows us to
# include another urls file in this one.
from django.urls import include  # new

urlpatterns = [
    path('admin/', admin.site.urls),

    # CHANGE: We want the root url (Ie anything after the first slash) to be
    # handled by our new 'pages' application. So we add a new `path` entry here,
    # that's blank (ie - there's nothing in the 'path', the part after the slash)
    # and tell it that everything below that point will be handled by *including*
    # the urls from our pages application.
    path("", include("pages.urls")),

]
