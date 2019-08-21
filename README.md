## Django Articles Website: "Da Fool"

**Overview**

This is a Django 2.2 example app featuring a homepage + article page. Article pages display article content retireved from a fake API and stock quote tickers from another fake API, as well as a Commenting feature providing the ability to post and delete comments as unauthenticated user. This commenting feature is a basic CRUD system built with Django models.

**Installation**
 
1. Clone this repo and navigate into the `dafool` directory
2. Create and activate a python3 virtualenv for this project (I used pipenv, a simplified virtual environment manager that work son Unix and Windows systems).

    a. To create a python3 virtualenv, from within the project directory, you need to run the command:

        `virualenv --python=/path/to/python3 .`

    b. Make sure your current version of python is at least python3.6 by running:

        `python --version`

    c. If you aren't using python3 by default, and don't know where you python3 is, run:
        `python3 --version` if that command works, run: `which python3` and that will display the `path/to/python3`

    Otherwise, you need to install python3.

    d. Once you've crated the virtualenv, from within that same project directory, run:

        `source bin/activate`

3. Run `./setup.sh` inside the `dafool` project directory
4. Run `python manage.py runserver` to start the Django server!

