import os, sys
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime

# Define the path to your SQLite database
basedir = os.path.abspath(os.path.dirname(__file__))
rootdir = os.path.abspath(os.path.join(basedir, '..', '..', '..'))
database_dir  = os.path.join(rootdir, 'database')
database_path = os.path.join(database_dir, 'Sellers_Hub.db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Define your database models
class Client(db.Model):
    client_CPF_ID = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50))
    phone_number = db.Column(db.String(20))
    email = db.Column(db.String(50))
    physical_address = db.Column(db.String(100))
    birthday = db.Column(db.Date)
    additional_information = db.Column(db.Text)

class Company(db.Model):
    company_CNPJ_ID = db.Column(db.Integer, primary_key=True)
    company_owner = db.Column(db.Integer, nullable=False)
    client_CPF_ID = db.Column(db.Integer, db.ForeignKey('client.client_CPF_ID'))

class Contract(db.Model):
    contract_id = db.Column(db.Integer, primary_key=True)
    contract_type = db.Column(db.String(50), nullable=False)
    administrator = db.Column(db.String(50))
    operator = db.Column(db.String(50))
    contract_plan = db.Column(db.String(50), nullable=False)
    data_inicio = db.Column(db.DateTime)
    data_fim = db.Column(db.DateTime)
    valor_contrato = db.Column(db.Numeric(10, 2))
    client_CPF_ID = db.Column(db.Integer, db.ForeignKey('client.client_CPF_ID'))

class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    first_pay_value = db.Column(db.Numeric(10, 2), nullable=False)
    extra_pay_value = db.Column(db.Numeric(10, 2))
    client_CPF_ID = db.Column(db.Integer, db.ForeignKey('client.client_CPF_ID'))


# Initialize Flask-Migrate
migrate = Migrate(app, db)

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/test-db')
def test_db():
    try:
        # Example: Querying the first record from the Client table
        client = Client.query.first()
        return f"Client name: {client.first_name} {client.last_name}"
    except Exception as e:
        return f"No client found in the databases"



if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
