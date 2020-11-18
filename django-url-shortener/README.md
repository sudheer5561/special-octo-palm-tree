# Django URL shortener

Example application that lets you define short links in the admin section,
then redirects visitors to the full link or returns 404 Not Found if no such
link exists.

## To set up locally for development

First, set up the Python libraries (you'll need Python 3 and PIP installed).

    pip3 install --user pipenv
    pipenv install
    pipenv shell

Now, you're in a shell where `python` can see the right libraries for this project.
Create the local SQLite database with the right schema by running

    ./manage.py migrate

Now, you can run the development server

    ./manage.py runserver

Going to the [admin interface](http://127.0.0.1:8000/admin/), you find out you
can't log in. The user is authenticated against a table in the local database.
Let's create one.

    ./manage.py createsuperuser

Now, you can create the link in admin and then go to
http://127.0.0.1:8000/your_short_link and be redirected.

## Deployment

When deploying to production, consider the [deployment checklist][dc], most notably:

- `settings.DEBUG = True` exposes too much information and makes it impossible
  to configure the look of the error pages.
- The settings reference the local SQLite database. Will it be performant enough?
  How to prevent data loss?
- Django needs to know the host name it will be deployed to (`settings.ALLOWED_HOSTS`),
  otherwise it refuses the request.
- What are the possible threats and drawbacks of serving this application over
  plain HTTP? Should we encrypt the traffic?

[dc]: https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
