from directories import db_path, add_dirs_to_sys_path
add_dirs_to_sys_path()

import os, sys
from flask import Flask
from flask_migrate import Migrate
from datetime import datetime
from database import db  # Import the db object from database.py
from models import *  # Import the models


app = Flask(__name__)           # Flask application object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)  # Initialize the db object with the app
migrate = Migrate(app, db)      # Flask-Migrate object

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
