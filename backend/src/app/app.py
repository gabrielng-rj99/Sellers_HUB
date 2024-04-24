from directories import *
from flask import Flask
from flask_migrate import Migrate
from models import *  # Import the models
from backend.src.app.database import db

app = Flask(__name__)       # Flask application object
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)            # Initialize the db object with the app
migrate = Migrate(app, db)  # Flask-Migrate object

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/test-db')
def test_db():
    try:
        # Querying all records from the Client table
        clients = Client.query.all()
        return [f"Client name: {client.first_name} {client.last_name}" for client in clients]
    except Exception as e:
        return f"No clients found in the database" 

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
