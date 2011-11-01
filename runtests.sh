#!/bin/bash

function start_server() {
    xterm -e "python manage.py runserver --settings=datawinners.settings_automated_testing" &
    sleep 2
}

echo "run functional test............"
xterm -e "python manage.py runserver" & sleep 2
pwd
cd func_tests
nosetests -a 'functional_test'
