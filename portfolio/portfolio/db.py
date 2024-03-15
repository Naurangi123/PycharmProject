import MySQLdb

database=MySQLdb.connect(
    host="localhost",
    user="root",
    password="naurangi@234",
)

cursor=database.cursor()

cursor.execute("CREATE DATABASE portfolioapp")

print("database connect")