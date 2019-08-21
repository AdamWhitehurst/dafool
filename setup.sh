#!/bin/bash

if [ "$VIRTUAL_ENV" == "" ]; then
    echo "ERROR: You must be in a VENV to run this script"
    exit 1
else
    # check that manage script has been created
    if [ ! -e "manage.py" ]; then
        python create_manage_script.py development
    fi

    # typical django startup routine
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py collectstatic

    echo
    echo
    echo '*************************************'
    echo 'Setup complete'
    echo 'run python manage.py runserver to start server'
    echo '*************************************'
    echo
    echo
fi