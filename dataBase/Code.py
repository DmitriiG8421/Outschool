import sqlite3 #This imports the SQLite library that allows you to interact with SQLite databases.

conn = sqlite3.connect("my_database.db") #This establishes a connection to a database file named my_database.db. If the file doesn't exist, it will be created.

cursor = conn.cursor()  #This creates a cursor object, which is used to interact with the database (executing queries, retrieving data, etc.).

cursor.execute("CREATE TABLE students (id INTEGER, name TEXT, grade INTEGER)")#This SQL command creates a table named students with three columns: id (integer type), name (text type), and grade (integer type).

cursor.execute("INSERT INTO students VALUES (1, 'Alice', 90)")#This inserts a row into the students table with id = 1, name = 'Alice', and grade = 90.  
 #This commits the changes, saving the new row into the table.
 
cursor.execute("SELECT * FROM students") #This SQL query retrieves all rows from the students table.
print(cursor.fetchall())#This prints all the rows returned by the SELECT query. fetchall() gets all the rows as a list of tuples.


conn.commit()#This saves the changes (commits them) to the database, ensuring the table is actually created.
conn.close()