seed:
	sudo docker-compose run web python manage.py seed

all-start:
	@echo "----- Starting All Services -----"
	sudo docker-compose up

down: 
	sudo docker-compose down

build:
	sudo docker-compose build

user:
	sudo docker-compose run web python manage.py createsuperuser

migrations:
	sudo docker-compose run web python manage.py makemigrations

migrate:
	sudo docker-compose run web python manage.py migrate