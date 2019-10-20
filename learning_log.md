Learning log - Python + django

# setup

- ideally get venv going
- on windows: set up python (currently 3.18)
- set up pip
- add both pyton and pip to path

```pip install django
python -m django --version // 2.2.6

django-admin // will show list of subcommands

django-admin startproject

```

//to run the site/server
python manage.py runserver

# conventions

everything in django is a separate app (as in, each route is called an app etc)

# creating apps and routes

python manage.py startapp [app_name]

within the blog directory, in views.py, we can create a view
note that when we add routes, our django app will stop defaulting to the default home page,
and we actually need to give it a default.

django will try to match routes in order.
first, it looks in the top level urls.py file.
whenever django encounters a pattern that matches, it sends to further processing to the appropriate url file.

- note that this is likely server side routing only, so our app wont be true spa and will reload on every new route.






