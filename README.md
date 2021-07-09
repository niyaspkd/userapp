django user CRUD
clone the repository

RUN

#to install all dependencies
pip install -r requirements.txt 

#create database if sqlite only create tables for others like postgres and mysql

python manage.py makemigrations 
python manage.py migrate

CREATE SUPERUSER

python manage.py createsuper user
python manage.py runserver

on the browser login to admin site using /admin

and go to the home page 127.0.0.1:8000 without login. all the api will be listed there

/users/login can be used to login and get token 

this token can be used in postman to acess edit, update and delete apis only the users can delete or update their own data


on /users/list  user can be created or listed also there will be search filters on browsable apu

cache used is of the builtin django cache and its set to 1 minute only for listing api


TEST CASES 


python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
....
----------------------------------------------------------------------
Ran 4 tests in 1.428s

OK
Destroying test database for alias 'default'...