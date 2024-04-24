from directories import *
add_dirs_to_sys_path()

import os, sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Client

# Create the engine to connect to the database
engine = create_engine(f'sqlite:///{db_path}')

# Create a sessionmaker bound to the engine
Session = sessionmaker(bind=engine)

# Create a new client
new_client = Client(first_name='John', last_name='Doe', phone_number='1234567890', email='john.doe@example.com')

# Add the new client to the database
with Session() as session:
    session.add(new_client)
    session.commit()