import os, psycopg2

connection = psycopg2.connect(user="accounting",
                                  password="Frostpin!2",
                                  host="localhost",
                                  database="fall2025csci260")

cursor =connection.cursor()

cursor.execute("Select * from common")

data=cursor.fetchall()

print(data)

