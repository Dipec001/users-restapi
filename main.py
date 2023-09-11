from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import re
from flask_migrate import Migrate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Create DB
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Users Table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    age = db.Column(db.String)
    nationality = db.Column(db.String(250))
    gender = db.Column(db.String(10))


with app.app_context():
    db.create_all()


# Route for adding a new person
@app.route('/api/add_person', methods=['POST'])
def add_person():
    # Get the JSON data from the request
    data = request.json

    # Validate data types and existence of 'name' field
    if 'name' not in data:
        return jsonify({'message': 'Name parameter is required'}), 400

    if not isinstance(data['name'], str):
        return jsonify({'message': 'Name should be a string'}), 400

    if 'age' in data and not isinstance(data['age'], str):
        return jsonify({'message': 'Age should be a string'}), 400

    if 'nationality' in data and not isinstance(data['nationality'], str):
        return jsonify({'message': 'Nationality should be a string'}), 400

    if 'gender' in data and not isinstance(data['gender'], str):
        return jsonify({'message': 'Gender should be a string'}), 400

    # Extract other optional parameters or set them to None if not provided
    name = data['name'].lower()
    age = data.get('age')
    nationality = data.get('nationality')
    gender = data.get('gender')

    # Normalize the name by reducing multiple spaces to a single space
    normalized_name = re.sub(r'\s+', ' ', name).strip()

    # Check if a user with the same name already exists
    existing_user = User.query.filter_by(name=normalized_name).first()

    if existing_user:
        # User with the same name already exists, return an error response
        return jsonify({'message': 'User with this name already exists'}), 400

    # Create a new User object and add it to the database
    new_user = User(name=normalized_name, age=age, nationality=nationality, gender=gender)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User added successfully'}), 201


# Route for fetching details of a person by name
@app.route('/api/get_person/<string:name>', methods=['GET'])
def get_person(name):
    if name is None:
        return jsonify({'message': 'Invalid request. Name parameter is missing'}), 400

    if not isinstance(name, str):
        return jsonify({'message': 'Invalid request. Name parameter should be a string'}), 400

    # Normalize the name by reducing multiple spaces to a single space
    normalized_name = re.sub(r'\s+', ' ', name).strip()

    if not normalized_name:
        return jsonify({'message': 'Name parameter is required'}), 400

    # Query the database to find the person by name
    person = User.query.filter_by(name=normalized_name.lower()).first()

    if person:
        # Person found, return their details
        person_data = {
            'name': person.name,
            'age': person.age,
            'nationality': person.nationality,
            'gender': person.gender
        }
        return jsonify(person_data), 200
    else:
        # Person not found, return an error response
        return jsonify({'message': 'Person not found'}), 404


# Route for updating details of an existing person by name
@app.route('/api/update_person/<string:name>', methods=['PUT'])
def update_person(name):
    # Get the JSON data from the request
    data = request.json

    # Normalize the provided existing name
    normalized_existing_name = re.sub(r'\s+', ' ', name).strip()

    # Check if a user with the provided existing name exists
    existing_user = User.query.filter_by(name=normalized_existing_name.lower()).first()

    if existing_user:
        # User with the existing name exists, proceed with the update

        # Extract the new name if provided
        new_name = data.get('new_name')

        if new_name:
            # Normalize the new name
            normalized_new_name = re.sub(r'\s+', ' ', new_name).strip()

            # Check if the new name already exists
            user_with_new_name = User.query.filter_by(name=normalized_new_name.lower()).first()

            if user_with_new_name:
                return jsonify({'message': 'New name already exists'}), 400

            # Update the name to the new name
            existing_user.name = normalized_new_name.lower()

        # Extract and update other optional parameters
        if 'age' in data:
            existing_user.age = data['age']
        if 'nationality' in data:
            existing_user.nationality = data['nationality']
        if 'gender' in data:
            existing_user.gender = data['gender']

        # Commit the changes to the database
        db.session.commit()

        return jsonify({'message': 'User updated successfully'}), 200
    else:
        # User with the provided existing name does not exist, return an error response
        return jsonify({'message': 'User not found'}), 404


# DELETE route for removing a person by name
@app.route('/api/delete_person/<string:name>', methods=['DELETE'])
def delete_person(name):
    if not name:
        return jsonify({'message': 'Name parameter is missing'}), 400

    if not isinstance(name, str):
        return jsonify({'message': 'Name should be a string'}), 400

    # Normalize the name by reducing multiple spaces to a single space
    normalized_name = re.sub(r'\s+', ' ', name).strip()

    # Query the database to find the person by name
    person = User.query.filter_by(name=normalized_name.lower()).first()

    if person:
        # Person found, remove them from the database
        db.session.delete(person)
        db.session.commit()
        return jsonify({'message': 'Person removed successfully'}), 200
    else:
        # Person not found, return an error response
        return jsonify({'message': 'Person not found'}), 404


if __name__ == "__main__":
    app.run(debug=False)
