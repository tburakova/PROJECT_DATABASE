import psycopg2


create_users_table = """
    DROP TABLE IF EXISTS users;
    CREATE TABLE users (
     id SERIAL PRIMARY KEY,
     fullname VARCHAR(100),
     email VARCHAR(100) UNIQUE
    );
    """

create_status_table = """
    DROP TABLE IF EXISTS status;
    CREATE TABLE status (
     id SERIAL PRIMARY KEY,
     name VARCHAR(100) UNIQUE
    );
    """

create_tasks_table = """
    DROP TABLE IF EXISTS tasks;
    CREATE TABLE tasks (
     id SERIAL PRIMARY KEY,
     title VARCHAR(100),
     description TEXT,
     status_id int,
     user_id int,
     FOREIGN KEY (status_id) REFERENCES status (id),
     FOREIGN KEY (user_id) REFERENCES users (id)
     ON DELETE CASCADE
    );
    """


connection = psycopg2.connect(
    database="", user='postgres',
    password='mysecretpassword', host='localhost', port=5432
)

cursor = connection.cursor()

cursor.execute(create_tasks_table)
connection.commit()