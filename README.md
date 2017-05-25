## Installing locally
1. INSTALL postgressql
  * Ubuntu: sudo apt-get install postgresql postgresql-contrib

2. Set-up Environment
  * virtualenv --no-site-packages Township-Website/
  * cd Township-Website/
  * source bin/activate
  * pip install -r requirements.txt

3. Set-up Database
  * psql
  * DROP DATABASE IF EXISTS township;
  * CREATE USER township;
  * CREATE DATABASE township OWNER township;
  * ctrl+d

  * python manage.py migrate --fake-initial

  * python manage.py createsuperuser

  * ctrl+d
