seed:
	docker-compose run web python manage.py seed

setup: build migrate superuser seed

all-start:
	@echo "----- Starting All Services -----"
	docker-compose up

down: 
	docker-compose down

build:
	docker-compose build

superuser:
	docker-compose run web python manage.py createsuperuser

migrations:
	docker-compose run web python manage.py makemigrations

migrate:
	docker-compose run web python manage.py migrate

test:
	docker-compose run web python manage.py test