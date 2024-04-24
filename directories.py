import sys, os

root_dir = os.path.abspath(os.path.dirname(__file__))
backend_dir = os.path.abspath(os.path.join(root_dir, 'backend',))
src_dir = os.path.abspath(os.path.join(root_dir, 'backend','src'))
app_dir = os.path.abspath(os.path.join(root_dir, 'backend','src', 'app'))
core_dir = os.path.abspath(os.path.join(root_dir, 'backend','src', 'core'))
functions_dir = os.path.abspath(os.path.join(root_dir, 'backend','src', 'functions'))
database_dir  = os.path.join(root_dir, 'database')

db_path = os.path.join(database_dir, 'Sellers_Hub.db')