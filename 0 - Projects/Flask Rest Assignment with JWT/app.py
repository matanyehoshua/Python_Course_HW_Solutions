from flask import Flask, request, Response, redirect, render_template, url_for, jsonify, make_response
import json
import logging
from Customers import Customers
from db_config import local_session, create_all_entities
from RepoDb import RepoDb
from User import User
from flask_sqlalchemy import SQLAlchemy
import uuid  # for public id
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import BigInteger, String, Column
import jwt
from datetime import datetime, timedelta
from functools import wraps
from configparser import ConfigParser

# log setup
for handler in logging.root.handlers:
    logging.root.removeHandler(handler)
config = ConfigParser()
config_read = config.read("config.conf")
LOG_LEVEL = config["logging"]["level"]
LOG_FILE_NAME_PREFIX = config["logging"]["logfile_name_prefix"]
LOG_FILE_NAME_EXT = config["logging"]["logfile_name_ext"]
logger = logging.getLogger("flask rest with jwt")

# creates an app that uses flask
app = Flask(__name__)
app.config['SECRET_KEY'] = 'S3CR3T' # this is the key
# database was made using pgAdmin 4 (postgresql)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:admin@localhost/Flask_Rest_Assignment_with_JWT' # database location
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
create_all_entities()
repo = RepoDb(local_session)
repo.reset_auto_inc(Customers)


# print(LOG_LEVEL)
# print(LOG_FILE_NAME_PREFIX)
# print(LOG_FILE_NAME_EXT)

logging.basicConfig(level=logging.INFO)

# initial values for the tables
repo.add(Customers(id=1, name='Dor', address='Rishon'))
repo.add(Customers(id=2, name='Nissim', address='Rehovot'))
repo.add(Customers(id=3, name='David', address='Tel-Aviv'))

customers = [{'id': 1, 'name': 'Dor', 'address': 'Rishon'},
             {'id': 2, 'name': 'Nissim', 'address': 'Rehovot'},
             {'id': 3, 'name': 'David', 'address': 'Tel-Aviv'}]

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            token = token.removeprefix('Bearer ')
            # long token is returned
        # return 401 if token is not passed
        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query \
                .filter_by(public_id=data['public_id']) \
                .first()
        except:
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401
        # passes the current logged in user into the endpoint so you have access to them
        # (you also just pass the data of the token, or whatever you want)
        return f(current_user, *args, **kwargs)
    return decorated

# main homepage
@app.route("/")
def home():
    logging.info('Entering homepage')
    return "<h1>This is the main homepage</h1>"

# GET, POST methods
# the operations are more "simplified" since there was an error when converting the new customer to dict
@app.route('/customers', methods=['GET', 'POST'])
@token_required
def get_or_post_customer():
    # sends a get method and if successful returns the status code 200
    if request.method == 'GET':
        all_customers = repo.get_all(Customers)
        all_customers_jsons = []
        for customer in all_customers:
            all_customers_jsons.append(customer.toObject())
        return Response(json.dumps(all_customers_jsons), status=200, mimetype='application/json')
    # sends a post method and if successful returns the status code 200
    if request.method == 'POST':
        new_customer = request.get_json()
        customers.append(new_customer)
        new_customer_model = Customers()
        new_customer_model.id = new_customer['id']
        new_customer_model.name = new_customer['name']
        new_customer_model.address = new_customer['address']
        repo.add(new_customer_model)
        return Response(status=200, mimetype='application/json')

# GET that returns token method
# the operations are more "simplified" since there was an error when converting the new customer to dict
@app.route('/customers/token', methods=['GET'])
def get_token():
    # sends a get method and if successful returns the status code 200
    if request.method == 'GET':
        all_customers = repo.get_all(Customers)
        all_customers_jsons = []
        for customer in all_customers:
            all_customers_jsons.append(customer.toObject())
        all_customers_jsons = jwt.encode({
            'exp': datetime.utcnow() + timedelta(minutes=30),
        }, app.config['SECRET_KEY'])
        return make_response(jsonify({'token': all_customers_jsons}), 201)

# GET/ID, PUT, DELETE, PATCH methods
@app.route('/customers/<int:id>', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
@token_required
# gets a customer by the id number
def get_customer_by_id(id):
    global customers
    if request.method == 'GET':
        for c in customers:
            if c["id"] == id:
                # if successful returns the status code 200
                return Response(json.dumps(c), status=200, mimetype='application/json')
        # if not successful returns the status code 404
        return Response(status=404, mimetype='application/json')
    # creates new data or replaces existing data using the Put Method
    if request.method == 'PUT':
        updated_new_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_new_customer["id"] if "id" in updated_new_customer.keys() else None
                c["name"] = updated_new_customer["name"] if "name" in updated_new_customer.keys() else None
                c["address"] = updated_new_customer["address"] if "address" in updated_new_customer.keys() else None
                # if the operation is successful returns the status code 200
                return Response(json.dumps(updated_new_customer, status=200, mimetype='application/json'))
    # creates new data or update/modify existing data using the Patch method
    if request.method == 'PATCH':
        updated_customer = request.get_json()
        for c in customers:
            if c["id"] == id:
                c["id"] = updated_customer["id"] if "id" in updated_customer.keys() else c["id"]
                c["name"] = updated_customer["name"] if "name" in updated_customer.keys() else c["name"]
                c["address"] = updated_customer["address"] if "address" in updated_customer.keys() else c["address"]
                # if the operation is successful returns the status code 200
                return Response(json.dumps(updated_customer, status=200, mimetype='application/json'))
        # if not successful returns the status code 404
        return Response(status=404, mimetype='application/json')
    if request.method == 'DELETE':
        customers = [c for c in customers if c["id"] != id]
        # if the operation is successful returns the status code 200
        return Response(json.dumps(customers), status=200, mimetype='application/json')

    class User(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        public_id = db.Column(db.String(50), unique=True)
        name = db.Column(db.String(100))
        email = db.Column(db.String(70), unique=True)
        password = db.Column(db.String(80))

@app.route('/signup', methods=['POST'])
def signup():
    form_data = request.form
    # gets username and password
    username = form_data.get('username')
    password = form_data.get('password')
# check if user exists
    user = User.query \
        .filter_by(username=username) \
        .first()
    if user:
        return make_response('User already exists. Please Log in.', 202)
    else:
        user = User(
            username=username,
            password=generate_password_hash(password)
        )
    db.session.add(user)
    db.session.commit()
    return make_response('Successfully registered.', 201)

@app.route('/login', methods=['POST'])
def login():
    form_data = request.form
    # gets username and password
    username = form_data.get('username')
    password = form_data.get('password')
    # check that no field is missing
    if not form_data or not username:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required!"'}
        )
    # check if user exists
    user = User.query \
        .filter_by(username=username) \
        .first()
    if not user:
        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Wrong Username or Password!"'}
        )
    # check password
    if not check_password_hash(user.password, password):
        return make_response(
            'Could not verify',
            403,
            {'WWW-Authenticate': 'Basic realm ="Wrong Username or Password!"'}
        )
    # generates the JWT Token
    token = jwt.encode({
        'exp': datetime.utcnow() + timedelta(minutes=30),
    }, app.config['SECRET_KEY'])
    return make_response(jsonify({'token': token}), 201)

@app.route('/users', methods=['GET'])
@token_required
def get_all_users(current_user):
    users = User.query.all()

    print(current_user.name)
    print(current_user.email)
    print(current_user.password)
    # convert to json
    output = []
    for user in users:
        output.append({
            'public_id': user.public_id,
            'name': user.name,
            'email': user.email
        })
    return jsonify({'users': output})


# this part must be at the bottom, otherwise a 404 error will occur:
if __name__ == "__main__":
    app.run()

