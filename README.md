# Users RESTful API Documentation

This is the documentation for the Users RESTful API developed by Divine Chukwu using Flask and SQLAlchemy.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [API Routes](#api-routes)
   - [Add a New Person](#add-a-new-person)
   - [Get Person Details by Name](#get-person-details-by-name)
   - [Get Person Details by Id](#get-person-details-by-id)
   - [Update Person Details by Name](#update-person-details-by-name)
   - [Update Person Details by Id](#update-person-details-by-id)
   - [Delete Person by Name](#delete-person-by-name)
   - [Delete Person by Id](#delete-person-by-id)
5. [Running the API](#running-the-api)
6. [Usage](#usage)
7. [Assumptions](#assumptions)
8. [API Doc with Postman](#api-doc-with-postman)


## Introduction

The Users RESTful API allows you to perform CRUD (Create, Read, Update, Delete) operations on user records. It provides endpoints for adding, retrieving, updating, and deleting user information.

## Prerequisites

Before you can set up and run the API, ensure that you have the following prerequisites installed:

- Python (version 3.10)
- Flask (version 1.1.2)
- Flask-SQLAlchemy (version 2.4.4)
- SQLite

You can install Python dependencies using pip:
Execute the command

pip install flask flask_sqlalchemy

## Setup

Clone this repository to your local machine: <br>
git clone https://github.com/Dipec001/users-restapi.git <br>
Navigate to your project directory <br>
cd users-restapi <br>
Install the required Python packages: <br>
pip install -r requirements.txt



## API Routes
Add a New Person <br>
**Endpoint:**  ```/api``` <br>
**HTTP Method:** POST <br>
**Description:** Adds a new person to the database. <br>
**Parameters:** JSON object with the following fields: <br>
name (string, required): The name of the person. <br>
age (string, optional): The age of the person. <br>
nationality (string, optional): The nationality of the person. <br>
gender (string, optional): The gender of the person. <br>
**Example Request:** <br>
```
POST  https://restfulapi-51bb862a3f02.herokuapp.com/api
Content-Type: application/json

{
  "name": "Divine chukwu",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}
```
**Example Response:** <br>
```
{
  "id" : 1,
  "name": "Divine chukwu",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}
```

Get Person Details by Name <br>
**Endpoint:**  ```/api/<string:name>``` <br>
**HTTP Method:** GET <br>
**Description:** Retrieves details of a person by their name. <br>
**Example Request:** <br>
```
GET  https://restfulapi-51bb862a3f02.herokuapp.com/api/Divine chukwu
```
**Example Response:** <br>
```
{
  "id" : 1,
  "name": "divine chukwu",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}
```
Get Person Details by Id <br>
**Endpoint:**  ```/api/user_id``` <br>
**HTTP Method:** GET <br>
**Description:** Retrieves details of a person by their id. <br>
**Example Request:** <br>
```
GET  https://restfulapi-51bb862a3f02.herokuapp.com/api/1
```
**Example Response:** <br>
```
{
  "id" : 1,
  "name": "divine chukwu",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}
```


Update Person Details By Name <br>
**Endpoint:**  ```/api/<string:name>``` <br>
**HTTP Method:** PUT <br>
**Description:** Updates details of an existing person by their name taken as a string in the url. If new_name is specified among the parameters, it updates the user's name too. <br>
**Parameters:** JSON object with the following fields: <br>
new_name (string, optional): The updated name of the person. <br>
age (string, optional): The updated age of the person. <br>
nationality (string, optional): The updated nationality of the person. <br>
gender (string, optional): The updated gender of the person. <br>
**Example Request:** <br>
```
PUT  https://restfulapi-51bb862a3f02.herokuapp.com/api/Divine chukwu
Content-Type: application/json

{
  "new_name": "C ronaldo",
  "age": "38",
  "nationality": "Portuguese",
  "gender": "Male"
}
```
**Example Response:** <br>
```
{
  "message": "User updated successfully"
}
```

Update Person Details By Id <br>
**Endpoint:**  ```/api/user_id``` <br>
**HTTP Method:** PUT <br>
**Description:** Updates details of an existing person by their Id passed in the url. If new_name is specified among the parameters, it updates the user's name too. <br>
**Parameters:** JSON object with the following fields: <br>
new_name (string, optional): The updated name of the person. <br>
age (string, optional): The updated age of the person. <br>
nationality (string, optional): The updated nationality of the person. <br>
gender (string, optional): The updated gender of the person. <br>
**Example Request:** <br>
```
PUT  https://restfulapi-51bb862a3f02.herokuapp.com/api/1
Content-Type: application/json

{
  "new_name": "C ronaldo",
  "age": "38",
  "nationality": "Portuguese",
  "gender": "Male"
}
```
**Example Response:** <br>
```
{
  "message": "User updated successfully"
}
```

Delete Person by Name <br>
**Endpoint:**  ```/api/<string:name>``` <br>
**HTTP Method:** DELETE <br>
**Description:** Deletes a person by their name. <br>
**Parameters:** The name parameter should be a string representing the person's name. <br>
**Example Request:** <br>
```
DELETE https://restfulapi-51bb862a3f02.herokuapp.com/api/Divine chukwu
```
**Example Response:** <br>
```
{
  "message": "Person removed successfully"
}
```

Delete Person by Id <br>
**Endpoint:**  ```/api/user_id``` <br>
**HTTP Method:** DELETE <br>
**Description:** Deletes a person by their Id. <br>
**Example Request:** <br>
```
DELETE https://restfulapi-51bb862a3f02.herokuapp.com/api/1
```
**Example Response:** <br>
```
{
  "message": "Person removed successfully"
}
```


## Running the API
To run the API locally, execute the following command: <br>
python main.py <br>

The API will be accessible at **http://127.0.0.1:5000/api** <br>

## Usage
You can use an HTTP clients like Postman to interact with the API. Refer to the API routes above for endpoint details. <br>

## Assummptions
- I assumed that the users have other attributes apart from their names. Attributes like age, nationality, gender.

## API Doc with Postman
Simple API doc which contains other example requests including headers to be passed <br>
<a href="https://documenter.getpostman.com/view/27596602/2s9YC2zYhr">Link to documentation</a>






