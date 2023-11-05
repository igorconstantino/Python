import sqlite3
from pathlib import Path


ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME
TABLE_NAME = 'customers'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

# SQL
cursor.execute(f'''
    DELETE FROM {TABLE_NAME}
''')
connection.commit()

cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {TABLE_NAME}
    (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    weight REAL
    )
''')
connection.commit()

sql = (f'''
    INSERT INTO {TABLE_NAME} (name, weight) VALUES
    (?, ?)
''')

cursor.executemany(
    sql,
    (('Igor', 67), ('Larissa', 50), ('Fabiana', 70), ('Robson', 90))
)
connection.commit()


cursor.execute(f'''
    SELECT * FROM {TABLE_NAME}
    WHERE name = "Igor" OR name = "Larissa"
''')

for row in cursor.fetchall():
    id_, name, weight = row
    print(f'id = {id_}, name = {name}, weight = {weight}')

cursor.close()
connection.close()
