seed:
	sudo docker-compose run web python manage.py seed

setup: build migrate superuser seed

all-start:
	@echo "----- Starting All Services -----"
	sudo docker-compose up

down: 
	sudo docker-compose down

build:
	sudo docker-compose build

superuser:
	sudo docker-compose run web python manage.py createsuperuser

migrations:
	sudo docker-compose run web python manage.py makemigrations

migrate:
	sudo docker-compose run web python manage.py migrate

test:
	sudo docker-compose run web python manage.py test