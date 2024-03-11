import MySQLdb

def initialize_connection():
    connection=MySQLdb.connect(host='localhost',user='root',password='rahul@1234')
    cursor=connection.cursor()
    return connection,cursor

def create_database(cursor):
    cursor.execute("show databases")
    temp=cursor.fetchall()
    databases=[item[0] for item in temp]

    if "register" not in databases:
        cursor.execute("create database register")
    cursor.execute("use register")

def create_table(cursor):
    cursor.execute("show tables")
    temp=cursor.fetchall()
    tables=[temp[0] for item in temp]

    if "login_data" not in tables:
        cursor.execute("""CREATE TABLE users(
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstName VARCHAR(100),
            lastName VARCHAR(100),
            password VARCHAR(30),
            email VARCHAR(100) UNIQUE,
            gender VARCHAR(1),
            age INT,
            address VARCHAR(200)
         )""")

def initialize_connection():
    connection=MySQLdb.connect(host='localhost',user='root',password='rahul@1234')
    cursor=connection.cursor()

    create_database(cursor)
    create_table(cursor)

    return connection,cursor
