![InsuranceFastAPI](/res/img/InsuranceFastAPI.svg)
___

💻 InsuranceFastAPI is a REST API service for calculating 
the cost of insurance depending on the type of cargo and 
the declared value.

## Features
- [X] Calculating the cost of insurance for the request using the current rate.
- [X] Returning (declared value * rate) depending on the type of cargo and date specified in the request.
- [X] There are ability to get, create, edit and delete information about rates.
- [X] There are a UI Documentation (Swagger) for API.

## Endpoints
The API has the following endpoints:

1. Insurance module:
    + `POST /insurance` for creating request for insurance.
    + `GET /insurance` for getting insurance history from Date Base.

2. Rate module:
     + `GET /rate/get/all` for getting information about all the rates from JSON file.
     + `GET /rate/get/{date}` for getting information about the rates on a specified date from JSON file.
     + `GET /rate/get/{date}/{cargo_type}` for getting information about the rate for a certain cargo on specified date from JSON file.
     + `POST /rate/add` for adding information about the new rate to JSON file
     + `PUT /rate/edit` for editing information about the existing rate in JSON file.
     + `DELETE /rate/delete/{date}` for deleting information about the rates on a specified date from JSON file.
     + `DELETE /rate/delete/{date}/{cargo_type}` for deleting information about the rate for a certain cargo on specified date from JSON file.
     
## Installation

For installation, you have to have docker and docker-compose.

You can change the ports using by the application and the database in the `docker-compose.yml` file. 
By default, the FastAPI application uses `8888`.   

1. Clone the repository: 
```
git clone https://github.com/ONEPANTSU/InsuranceFastAPI.git
```
2. Create an environment file `.env-deploy` in the root directory and fill it with the following variables:
```python
#   Example of the environment file

DB_HOST=db
DB_PORT=5435    #   Use the same port as in the docker-compose.yml
DB_NAME=insurance
DB_USER=postgres
DB_PASSWD=postgres

POSTGRES_DB="insurance"
POSTGRES_USER="postgres"
POSTGRES_PASSWORD="postgres"
```
3. Build the docker-compose file:
```
docker-compose build
```
4. Run it with:
```
docker-compose up
```
5. The API will be able by the link: `http://<IP>:<PORT>`
6. The Swagger will be able by the link: `http://<IP>:<PORT>/docs`


## Technologies
- FastAPI
- Tortoise ORM
- PostgreSQL
- Docker
- Docker-compose
