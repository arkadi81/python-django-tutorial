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

# Templates and passing data to/from templates

per django convention, we will need to create a `\templates\app_name` directory in our app directory. django will look for templates in all installed applications' template folder.

* We also have to add our application to the list of installed apps for django to know about it and look for templates inside of it. to do so, go to app_name\apps.py

* passing information to templates is done via the context parameter as in
```context = {
		'posts': posts
	}
	return render(request, 'blog/home.html',context)
```
* the templating engine django uses is very similar to jinja2. Allows to have logic and inclusion of variables in html.
** for loops
``` {% for post in posts %}
		<h1>{{post.title}}</h1>
	{% endfor %}
```
** if / else logic
```	{% if title %}
		html code..
	{% else %}
		other html code..
	{% endif %}
```

# Template inharitance and avoiding repetition (similar to component tree in react)

* create blocks within existing templates that child templates can take over using
``` {% block block_name %} { % endbllock % } ```

* use parent templates by 
``` { % extends "blog/base.html %}
	{% block content %}
		stuff...
	{% endblock content %}
```







