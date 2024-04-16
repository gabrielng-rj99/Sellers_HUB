from sqlalchemy import create_engine, text
database_path = 'database'

if __name__ == '__main__':
    # Create an engine to connect to your database
    engine = create_engine('sqlite:///' + database_path)

    # Establish a connection
    connection = engine.connect()

    # Execute the query
    result = connection.execute(text("SELECT name FROM sqlite_master WHERE type='table' AND name='Client'"))

    # Fetch the result
    table_exists = result.fetchone() is not None

    # Close the connection
    connection.close()

    # Print the result
    if table_exists:
        print("The table exists.")
    else:
        print("The table does not exist.")