# Portal Telemedicina - Data Warehouse

## Solutions Architecture
---
The project is developed with Django, Django Rest Framework, Postgres and it was set up in a docker/docker-compose enviroment with the help of a make file to run the project.
For the developer to see and manage the data, Django Admin can be used, for better usage, it was added a filter for the exams by the altered status.

The API provides routes of patients, doctors, exam-types and examinations. All routes requires authentication. Once a user is added in admin, it is possible to generate the token authorization by the authenticaion routes.

The project also has implemented flake8 linter for the PR's and unit tests.

The 'make setup' command is responsible to build the images, run the migration, create the superuser and populate the database.

---


## Local Project Setup  


### Setup and Populate Database

```make setup```

### Create Super User
  
```make superuser```

### Run Tests

```make test```

### Run Application
```make all-start```

---

## API 

## - Authentication Routes  

#### After create user by admin, retrieve the token, passing the body to the request:  


```
{
    "username": <username>,
    "password"": <password>
}
```


[POST]  ```http://localhost:8000/api/v1/token-auth/```  


## - Business Logic Routes   



### You must add token authorization to the request:  


```
{
    "Authorization": "Token <token>"
}
```
### Examinations Endpoints:
| METHOD      | ENDPOINT | DESCRIPTION |
| :---:        |    :----:   | :----: |
| GET      |```http://localhost:8000/api/v1/examinations/```| List all examinations |
| GET | ```http://localhost:8000/api/v1/examinations/<id>```| Retrieve an examination|
| GET      |```http://localhost:8000/api/v1/examinations?altered=true```| List altered examinations |
| GET | ```http://localhost:8000/api/v1/examinations?altered=false```|List not altered examinations|
| POST      |```http://localhost:8000/api/v1/examinations/```| Add an examination|
| DELETE | ```http://localhost:8000/api/v1/examinations/<id>```| Delete an examination| 
| UPDATE | ```http://localhost:8000/api/v1/examinations/<id>```| Update an examination|



### Patients Endpoints:
| METHOD      | ENDPOINT | DESCRIPTION |
| :---:        |    :----:   | :----: |
| GET      |```http://localhost:8000/api/v1/patients/```| List all patients |
| GET | ```http://localhost:8000/api/v1/patients/<id>```| Retrieve a patient|
| POST      |```http://localhost:8000/api/v1/patients/```| Add a patient|
| DELETE | ```http://localhost:8000/api/v1/patients/<id>```| Delete a patient| 
| UPDATE | ```http://localhost:8000/api/v1/patients/<id>```| Update a patient|

### Doctors Endpoints:
| METHOD      | ENDPOINT | DESCRIPTION |
| :---:        |    :----:   | :----: |
| GET      |```http://localhost:8000/api/v1/doctors/```| List all doctors |
| GET | ```http://localhost:8000/api/v1/doctors/<id>```| Retrieve a doctor|
| POST      |```http://localhost:8000/api/v1/doctors/```| Add a doctor|
| DELETE | ```http://localhost:8000/api/v1/doctors/<id>```| Delete a doctor| 
| UPDATE | ```http://localhost:8000/api/v1/doctors/<id>```| Update a doctor|

### Exam Type Endpoints:
| METHOD      | ENDPOINT | DESCRIPTION |
| :---:        |    :----:   | :----: |
| GET      |```http://localhost:8000/api/v1/exam-types/```| List all exam types |
| GET | ```http://localhost:8000/api/v1/exam-types/<id>```| Retrieve a exam type|
| POST      |```http://localhost:8000/api/v1/exam-types/```| Add a exam type|
| DELETE | ```http://localhost:8000/api/v1/exam-types/<id>```| Delete a exam type| 
| UPDATE | ```http://localhost:8000/api/v1/exam-types/<id>```| Update a exam type|