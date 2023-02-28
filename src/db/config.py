import sqlite3 
con = sqlite3.connect("danceholicsve.db")

cur = con.cursor()

res = cur.execute('SELECT * FROM sqlite_master WHERE type = "table";')
table = res.fetchone()

if not table: 
    cur.execute("""CREATE TABLE clases (
  id int,
  genero int,
  instructor int,
  sede int,
  horario timestamp,
  created at varchar(255)
);""")

cur.execute("""CREATE TABLE instructores (
  id int,
  nombre varchar(255),
  email varchar(255),
  genero varchar(255)
);""")

cur.execute("""CREATE TABLE sedes (
  id int,
  nombre varchar(255)
);""")

cur.execute("""CREATE TABLE generos_baile (
  id int,
  nombre varchar(255)
);""")

cur.execute("ALTER TABLE clases ADD FOREIGN KEY (genero) REFERENCES generos_baile (id);")

cur.execute("ALTER TABLE clases ADD FOREIGN KEY (instructor) REFERENCES instructores (id);")

cur.execute("ALTER TABLE clases ADD FOREIGN KEY (sede) REFERENCES sedes (id);")

cur.execute("""CREATE TABLE instructores_generos_baile (
  instructores_id int,
  generos_baile_id int,
  PRIMARY KEY (instructores_id, generos_baile_id)
);""")

cur.execute("ALTER TABLE instructores_generos_baile ADD FOREIGN KEY (instructores_id) REFERENCES instructores (id);")

cur.execute("ALTER TABLE instructores_generos_baile ADD FOREIGN KEY (generos_baile_id) REFERENCES generos_baile (id);")


cur.execute("""CREATE TABLE instructores_sedes (
  instructores_id int,
  sedes_id int,
  PRIMARY KEY (instructores_id, sedes_id)
);""")

cur.execute("ALTER TABLE instructores_sedes ADD FOREIGN KEY (instructores_id) REFERENCES instructores (id);")

cur.execute("ALTER TABLE instructores_sedes ADD FOREIGN KEY (sedes_id) REFERENCES sedes (id);")
