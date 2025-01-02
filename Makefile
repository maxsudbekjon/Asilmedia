mig:
	python ./manage.py makemigrations
	python ./manage.py migrate
create:
	python ./manage.py createsuperuser
