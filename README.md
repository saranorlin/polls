# Django Polls Tutorial 
https://docs.djangoproject.com/en/4.2/intro/tutorial02/

## Getting started
- `pipenv shell`
- `python manage.py runserver` 

## Intial DB setup
https://www.sqlshack.com/setting-up-a-postgresql-database-on-mac/
- `brew services start postgresql`
- `psql postgres`
- `CREATE ROLE polluser WITH LOGIN PASSWORD 'password';`
- `ALTER ROLE polluser CREATEDB;`
- `CREATE DATABASE poll_db;`


Start here: https://docs.djangoproject.com/en/4.2/intro/tutorial02/#creating-models