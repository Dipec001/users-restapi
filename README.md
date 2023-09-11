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

Clone this repository to your local machine:
git clone https://github.com/Dipec001/users-restapi.git
Navigate to your project directory
cd users-restapi
Install the required Python packages:
pip install -r requirements.txt



## API Routes
Add a New Person
**Endpoint:** /api/add_person
**HTTP Method:** POST
**Description:** Adds a new person to the database.
**Parameters:** JSON object with the following fields:
name (string, required): The name of the person.
age (string, optional): The age of the person.
nationality (string, optional): The nationality of the person.
gender (string, optional): The gender of the person.
**Example Request:**
{
  "name": "John Doe",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}
**Example Response:**
{
  "message": "User added successfully"
}

Get Person Details by Name
**Endpoint:** /api/get_person/<string:name>
**HTTP Method:** GET
**Description:** Retrieves details of a person by their name.
**Parameters:** The name parameter should be a string representing the person's name.
**Example Request:**
GET /api/get_person/John%20Doe
**Example Response:**
{
  "name": "John Doe",
  "age": "30",
  "nationality": "American",
  "gender": "Male"
}


Update Person Details
**Endpoint:** /api/update_person
**HTTP Method:** PUT
**Description:** Updates details of an existing person by their name.
**Parameters:** JSON object with the following fields:
name (string, required): The name of the person to update.
age (string, optional): The updated age of the person.
nationality (string, optional): The updated nationality of the person.
gender (string, optional): The updated gender of the person.
**Example Request:**
{
  "name": "John Doe",
  "age": "31",
  "nationality": "American",
  "gender": "Male"
}
**Example Response:**
{
  "message": "User updated successfully"
}


Delete Person by Name
**Endpoint:** /api/delete_person/<string:name>
**HTTP Method:** DELETE
**Description:** Deletes a person by their name.
**Parameters:** The name parameter should be a string representing the person's name.
**Example Request:**
DELETE /api/delete_person/John%20Doe
**Example Response:**
{
  "message": "Person removed successfully"
}


## Running the API
To run the API locally, execute the following command:
python main.py

The API will be accessible at **http://127.0.0.1:5000**

## Usage
You can use an HTTP clients like Postman to interact with the API. Refer to the API routes above for endpoint details.



