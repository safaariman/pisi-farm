# Pisi Build Farm

Brand new Pisi Build Farm for Pisilinux.

## How to install

```bash
$ virtualenv -p /usr/bin/python3.6 venv
$ source venv/bin/activate
(venv) $ pip install pip-tools
(venv) $ pip-sync
(venv) $ python manage.py migrate
(venv) $ python manage.py loaddata initial_user
(venv) $ python manage.py compilemessages
```

## Running the development server

```bash
(venv) $ python manage.py runserver
```

## Access the development server

You can access to the development server from http://localhost:8000/admin using username `pisi` and password `isip` 