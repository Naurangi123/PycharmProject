import MySQLdb


def initialize_connection():
    conn = MySQLdb.connect(
        host="localhost",
        user="root",
        password="rahul@1234"
    )

    cursor = conn.cursor()
    create_database(cursor)
    create_table(cursor)

    return conn, cursor


def create_database(cursor):
    cursor.execute("SHOW DATABASES")
    temp = cursor.fetchall()
    databases = [item[0] for item in temp]

    if "register" not in databases:
        cursor.execute("CREATE DATABASE register")

    cursor.execute("USE register")


def create_table(cursor):
    cursor.execute("SHOW TABLES")
    temp = cursor.fetchall()
    tables = [item[0] for item in temp]

    if "login_data" not in tables:
        cursor.execute("""CREATE TABLE login_data(
            id INT AUTO_INCREMENT PRIMARY KEY,
            firstName VARCHAR(100),
            lastName VARCHAR(100),
            password VARCHAR(30),
            email VARCHAR(100) UNIQUE,
            gender VARCHAR(1),
            age INT,
            address VARCHAR(200)
         )""")


def login(cursor, data):
    cursor.execute(f"""SELECT * FROM login_data WHERE email = '{data["email"]}' 
                       AND password = '{data["password"]}' """)

    if cursor.fetchone() != None:
        return True
    return False


def register(cursor, conn, data):
    print(data)

    cursor.execute(f"""INSERT INTO login_data values( 
        NULL,
        '{data["firstName"]}', 
        '{data["lastName"]}', 
        '{data["password"]}', 
        '{data["email"]}', 
        '{data["gender"]}', 
        '{data["age"]}', 
        '{data["address"]}'
    )""")

    conn.commit()