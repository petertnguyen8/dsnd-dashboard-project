from sqlite3 import connect
from pathlib import Path
from functools import wraps
import pandas as pd

# Using pathlib, create a `db_path` variable
# that points to the absolute path for the `employee_events.db` file
db_path = Path(__file__).parent / 'employee_events.db'
print('this is the db path:', db_path)

connection = connect(db_path)
print(connection)