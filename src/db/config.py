import sqlite3 
import pathlib
from typing import Tuple

def start_db() -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
  con = sqlite3.connect("danceholicsve.db")
  cur = con.cursor()

  res = cur.execute('SELECT * FROM sqlite_master WHERE type = "table";')
  table = res.fetchone()

  if not table:
    print(table)
    current_path = pathlib.Path().resolve()
    tables_file = open(str(current_path) + "/src/db/db_initial_query.txt", "r")
    initial_query = tables_file.read()
    for statement in initial_query.split(";"):
      print(statement)
      if not statement: continue
      cur.execute(statement)

    data_file = open(str(current_path) + "/src/db/db_data_query.txt", "r")
    intial_data = data_file.read()
    for statement in intial_data.split(";"):
      print(statement)
      cur.execute(statement)
      con.commit()

  return con, cur
