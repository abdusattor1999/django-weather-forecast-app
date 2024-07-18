This app has build in django to know forecast infos for queried city

To run this app in local machine:
1 - clone the repo from github
2 - make local environment like pipenv or venv (python -m venv env)
3 - install required packages with command: 
>>> pip install -r reqs.txt

4 - migrate with database:
>>> python manage.py migrate

5 - Here is almost done you can run the project:
>>> python manage.py runserver