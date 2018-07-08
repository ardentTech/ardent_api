#!/bin/bash

DB_NAME="ardent"
DJANGO="$(pwd)/api"
PM="python manage.py"
# @todo make "dev|pro" an arg
SETTINGS="--settings=api.settings.dev"

build() {
    echo
    echo "########### BUILD ###########"
    dropdb ardent
    createdb ardent
    makemigrations
    migrate
    test
}

createsuperuser() {
    echo
    echo "########### CREATE SUPER USER ###########"
    cd ${DJANGO} && ${PM} createsuperuser ${SETTINGS}
}

makemigrations() {
    echo
    echo "########### MAKE MIGRATIONS ###########"
    cd ${DJANGO} && ${PM} makemigrations ${SETTINGS}
}

migrate() {
    echo
    echo "########### MIGRATE ###########"
    cd ${DJANGO} && ${PM} migrate ${SETTINGS}
}

server() {
    echo
    echo "########### SERVER ###########"
    cd ${DJANGO} && ${PM} runserver ${SETTINGS}
}

test() {
    echo
    echo "########### TEST ###########"
    cd ${DJANGO} && ${PM} test ${SETTINGS}
}

source ./venv/bin/activate
${1}

echo
echo "DONE!"
exit 0
