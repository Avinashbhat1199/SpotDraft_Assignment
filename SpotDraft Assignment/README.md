

A simple favorites app that lets us view/favorite Star Wars data. The data is loaded from the JSON API https://swapi.co/. 

## Running the Server

1. Install the requirements with the command `pip install -r requirements.txt`
2. DB setup need set flask variable- $env:FLASK_APP ="app.py"
3. db migration run commands -  flask db init 
                                                   flask db migrate -m " comment"
                                                   flask db upgrade


The API will now be available http://localhost:5000/

## Endpoints

The following Endpoints are available in the API.

#List Planets

Endpoint: `/planets`

Method: GET

#List Movies

Endpoint: `/movies`

Method: GET

#Add Favorite planet

Endpoint: `/favorites/planet`

Method: POST

Input Data:
{
"id":"id" must,
"planetname": "planetname",
"customname":null or "value"}

#Add Favorite movie

Endpoint: `/favorites/movie`

Method: POST

Input Data:
{
"id":"id" must,
"moviename": "moviename",
"customname":null or "value"}

#Search Movie

Endpoint: `/search/movie`

Method: POST

Input Data:
{

"title": "moviename",
"customname":null or "value"}


#Search Movie

Endpoint: `/search/planet`

Method: POST

Input Data:
{

"name': "planetname",
"customname":null or "value"}


