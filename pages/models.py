from django.db import models

# CHANGE: Let's create some objects to display in our pages. In a 'real' django app
# This would probably look quite different - our objects would come from records in a database
# perhaps, and the code here would describe how to connect to it. In our case, we don't want
# to bother with all that complexity just yet, so we're going to make some very simple python
# objects directly, which represent the objects shown on our page. In this case, we're
# going to make a page about fruit. We start with a 'class' that represents, in the
# abstract, what a fruit is like - it has a name, color, and weight.
class Fruit:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight

# We then useuse our new class to create a few concrete examples of fruit that we want to display
apple = Fruit("Apple", "red", 200)
orange = Fruit("Orange", "orange", 140)
banana = Fruit("Banana", "yellow", 120)

# And finally we create a list of all the fruit in our system, which we can then display on our page.
all_fruit = [apple, orange, banana]
