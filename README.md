
# NewsApp

A web app made using the `django` framework. Frontend using `html` and `bootstrap` and `PostgresSQL` is used as the database. You can add articles which can be viewed by anyone. Just make an account and you are good to go.

## Requirements

Python 3.8  
Django 3.2  
Docker and docker-compose

## Setting up the Project

  * Download and install Python 3.8
  * Download and install Docker and docker-compose
  * Download and install Git.
  * Fork the Repository.
  * Clone the repository to your local machine `$ git clone https://github.com/AlymbekovvDastan/newsApp.git`
  * Change directory to newsApp `$ cd newsApp`
  * Build images `$ docker-compose build`  
  * Run the project `$ docker-compose up --d`  
  * Create superuser `$ docker-compose exec web python ./manage.py createsuperuser`


