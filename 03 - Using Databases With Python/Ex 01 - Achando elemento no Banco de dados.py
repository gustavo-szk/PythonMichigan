# If you don't already have it, install the SQLite Browser from http://sqlitebrowser.org/.

# Then, create a SQLITE database or use an existing database and create a table in the database called "Ages":

#  CREATE TABLE Ages ( 
#  name VARCHAR(128), 
#  age INTEGER
#  )
# Then make sure the table is empty by deleting any rows that you previously inserted, and insert these rows and only these rows with the following commands:

# DELETE FROM Ages;
# INSERT INTO Ages (name, age) VALUES ('Matej', 29);
# INSERT INTO Ages (name, age) VALUES ('Sally', 33);
# INSERT INTO Ages (name, age) VALUES ('Hind', 34);
# INSERT INTO Ages (name, age) VALUES ('Keivlin', 26);
# INSERT INTO Ages (name, age) VALUES ('Samarjit', 19);
# INSERT INTO Ages (name, age) VALUES ('Prentice', 33);
# Once the inserts are done, run the following SQL command:
# SELECT hex(name || age) AS X FROM Ages ORDER BY X
# Find the first row in the resulting record set and enter the long string that looks like 53656C696E613333.

import sqlite3
conectando = sqlite3.connect(':memory:')

c = conectando.cursor()
c.execute("""CREATE TABLE Ages(
             name VARCHAR(128),
             age INTEGER
             )"""
         )

def add_pessoas(sNome, iIdade):
    with conectando:
        c.execute("INSERT INTO Ages VALUES (:name, :age)", {'name':sNome, 'age':iIdade})

lPessoas = [('Oz', 25), ('Noor', 31), ('Praise', 22), ('Kerris', 26), ('Louise', 19), ('Ismaeel', 17)]

for tItem in lPessoas:
    sNome, iIdade = tItem
    add_pessoas(sNome, iIdade)

c.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")

print(c.fetchall())

conectando.commit()
conectando.close()