## Notes
- docker build .
- docker-compose build
- docker-compose run app sh -c "django-admin.py startproject app ."
- .travis.yml is the default conf file to syn with the CI tool Travis-C
- Django framework searchs for files where name start with 'test' to test created functions.
- Functions to test on the tests files, should also named as test_....
- docker-compose run app sh -c "python manage.py test"
- docker-compose run app sh -c "python manage.py startapp core"
- docker-compose run app sh -c "python manage.py makemigrations core"
- docker-compose run app sh -c "python manage.py test && flake8"
- Mocking:  test without depend on other services, like fake sending and email
- docker-compose up
- docker-compose run app sh -c "python manage.py createsuperuser"
- docker-compose run --rm app sh -c "python manage.py startapp user"
- docker-compose run --rm app sh -c "python manage.py test && flake8"
- docker-compose run --rm app sh -c "python manage.py startapp recipe"
docker-compose run --rm app sh -c "python manage.py makemigrations core"