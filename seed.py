import psycopg2
from faker import Faker
import random


connection = psycopg2.connect(
    database="", user='postgres',
    password='mysecretpassword', host='localhost', port=5432
)

cursor = connection.cursor()

# Створення курсора
cur = connection.cursor()

# Ініціалізація Faker
fake = Faker()


# Заповнення таблиці users
for u in range(10):  # Імітуємо 10 користувачів
    fullname = fake.name()
    email = fake.email()
    cursor.execute("INSERT INTO users (fullname, email) VALUES (%s, %s)", (fullname, email))

# Заповнення таблиці status
status_names = ["New", "In Progress", "Completed"]
for status_name in status_names:
    cur.execute("INSERT INTO status (name) VALUES (%s)", (status_name,))

# Отримання списку користувачів та статусів
cur.execute("SELECT id FROM users")
user_ids = [row[0] for row in cur.fetchall()]

cur.execute("SELECT id FROM status")
status_ids = [row[0] for row in cur.fetchall()]

# Заповнення таблиці tasks
for t in range(20):  # Імітуємо 20 завдань
    title = fake.sentence()
    description = fake.paragraph()
    status_id = random.choice(status_ids)
    user_id = random.choice(user_ids)
    cur.execute("INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id))

# Збереження змін у базі даних
connection.commit()






