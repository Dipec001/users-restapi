# Users RESTful API Documentation

This is the documentation for the Users RESTful API developed by Divine Chukwu using Flask and SQLAlchemy.

## Table of Contents

1. [Introduction](#introduction)
2. [Prerequisites](#prerequisites)
3. [Setup](#setup)
4. [API Routes](#api-routes)
   - [Add a New Person](#add-a-new-person)
   - [Get Person Details by Name](#get-person-details-by-name)
   - [Update Person Details](#update-person-details)
   - [Delete Person by Name](#delete-person-by-name)
5. [Running the API](#running-the-api)
6. [Usage](#usage)


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
**Endpoint:** /api/add_person <br>
**HTTP Method:** POST <br>
**Description:** Adds a new person to the database. <br>
**Parameters:** JSON object with the following fields: <br>
name (string, required): The name of the person. <br>
age (string, optional): The age of the person. <br>
nationality (string, optional): The nationality of the person. <br>
gender (string, optional): The gender of the person. <br>
**Example Request:** <br>
{ <br>
  "name": "John Doe", <br>
  "age": "30", <br>
  "nationality": "American", <br>
  "gender": "Male" <br>
} <br>
**Example Response:** <br>
{ <br>
  "message": "User added successfully" <br>
} <br>

Get Person Details by Name <br>
**Endpoint:** /api/get_person/<string:name> <br>
**HTTP Method:** GET <br>
**Description:** Retrieves details of a person by their name. <br>
**Parameters:** The name parameter should be a string representing the person's name. <br>
**Example Request:** <br>
GET /api/get_person/John%20Doe <br>
**Example Response:** <br>
{ <br>
   "name": "John Doe", <br>
   "age": "30", <br>
   "nationality": "American", <br>
   "gender": "Male" <br>
} <br>


Update Person Details <br>
**Endpoint:** /api/update_person <br>
**HTTP Method:** PUT <br>
**Description:** Updates details of an existing person by their name. <br>
**Parameters:** JSON object with the following fields: <br>
name (string, required): The name of the person to update. <br>
age (string, optional): The updated age of the person. <br>
nationality (string, optional): The updated nationality of the person. <br>
gender (string, optional): The updated gender of the person. <br>
**Example Request:** <br>
{ <br>
  "name": "John Doe", <br>
  "age": "31", <br>
  "nationality": "American", <br>
  "gender": "Male" <br>
} <br>
**Example Response:** <br>
{ <br>
  "message": "User updated successfully" <br>
} <br>


Delete Person by Name <br>
**Endpoint:** /api/delete_person/<string:name> <br>
**HTTP Method:** DELETE <br>
**Description:** Deletes a person by their name. <br>
**Parameters:** The name parameter should be a string representing the person's name. <br>
**Example Request:** <br>
DELETE /api/delete_person/John%20Doe <br>
**Example Response:** <br>
{ <br>
  "message": "Person removed successfully" <br>
} <br>


## Running the API <br>
To run the API locally, execute the following command: <br>
python main.py <br>

The API will be accessible at **http://127.0.0.1:5000** <br>

## Usage <br>
You can use an HTTP clients like Postman to interact with the API. Refer to the API routes above for endpoint details.



