# Pisi Build Farm

Brand new Pisi Build Farm for Pisilinux.

## How to install

```bash
$ pipenv install
$ pipenv run python manage.py migrate
$ pipenv run python manage.py loaddata initial_user
$ pipenv run python manage.py compilemessages
```

## Running the development server

```bash
$ pipenv run python manage.py runserver
```

## Access the development server

You can access to the development server from http://localhost:8000/admin using username `pisi` and password `isip` 