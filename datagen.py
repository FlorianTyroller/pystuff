from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from random import randint, choice
import string
from faker import Faker

import mysql.connector
from mysql.connector import Error

def create_u(user_id, email, first_name, last_name, password):
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='springuser',
            password='ThePassword',
            database='db_example'
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO user (id, email, first_name, last_name, password) 
                            VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (user_id, email, first_name, last_name, password))
        insert_query2 = """INSERT INTO user_member_in_clubs (members_id, member_in_clubs_id) VALUES (%s, %s)"""
        cursor.execute(insert_query2, (user_id, 10))
        connection.commit()
        print("User created successfully")
    except mysql.connector.Error as error:
        print("Failed to create user: {}".format(error))
    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()


# generate some random data
fake = Faker()
users = []
for a in range(100, 200):
    u = [a, fake.email(), fake.first_name(), fake.last_name(), ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))]
    users.append(u)

for user in users:
    print(user)
    create_u(user[0], user[1], user[2], user[3], user[4])

