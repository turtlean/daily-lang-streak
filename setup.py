import os 
import sqlite3
from sqlite3 import Error

DB_NAME = 'dictionary.db'
dir_path = os.path.dirname(os.path.realpath(__file__))
conn = sqlite3.connect(dir_path + '/' + DB_NAME)

sql_create_entries_table = """                              
                              CREATE TABLE IF NOT EXISTS entries (
                                	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                  expression TEXT,
                                  context TEXT,
                                  meaning TEXT,
                                  example TEXT,
                                  extra TEXT,
                                  keywords TEXT,
                                  score	INTEGER
                              ); 
                            """

try: 
  conn.cursor().execute(sql_create_entries_table)
  print("Dictionary database successfully initialized ⭐️")
except Error as e:
  print("Error! cannot create the database connection: ")
  print(e)

conn.commit()
conn.close()
