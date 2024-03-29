from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from random import randint, choice
import string
from faker import Faker

import mysql.connector
from mysql.connector import Error

fake = Faker()

connection = mysql.connector.connect(
            host='localhost',
            user='springuser',
            password='ThePassword',
            database='db_example'
        )
cursor = connection.cursor()

offset = 10000

# create clubs
club_count = 10
for i in range(offset, offset + club_count):
    c_name = fake.company()
    c_id = i + 1
    q = "INSERT INTO club (id, name) VALUES (%s, %s)"
    cursor.execute(q, (c_id, c_name))
    connection.commit()

# create trainings
training_count = 100
for i in range(offset, offset + training_count):
    t_id = i + 1
    t_descritpion = fake.text()
    # endtime is between 1 and 3 hours after starttime and in the next 14 days hour is between 6 and 20
    t_start_time = fake.date_time_between(start_date='+0d', end_date='+14d', tzinfo=None) 
    t_star = t_start_time.hour
    while t_star < 6 or t_star > 19:
        t_start_time = fake.date_time_between(start_date='+0d', end_date='+14d', tzinfo=None) 
        t_star = t_start_time.hour
    
    # endtime is between 1 and 3 hours after starttime
    t_end_time = t_start_time
    t_end_time = t_end_time.replace(hour=t_end_time.hour + randint(1, 3))
    t_location = fake.address()
    t_title = fake.sentence(nb_words=6, variable_nb_words=True)
    t_club_id = randint(offset + 1, offset + club_count)
    q = "INSERT INTO training (id, description, end_time, location, start_time, title, club_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(q, (t_id, t_descritpion, t_end_time, t_location, t_start_time, t_title, t_club_id))
    connection.commit()


# create users
user_count = 1000
for i in range(offset, offset + user_count):
    u_email = fake.email()
    u_first_name = fake.first_name()
    u_last_name = fake.last_name()
    u_password = ''.join(choice(string.ascii_letters + string.digits) for _ in range(10))
    u_id = i + 1
    q = "INSERT INTO user (id, email, first_name, last_name, password) VALUES (%s, %s, %s, %s, %s)" 
    cursor.execute(q, (u_id, u_email, u_first_name, u_last_name, u_password))
    connection.commit()

    # create user_member_in_clubs
    club_id = randint(offset + 1, offset + club_count)
    q = "INSERT INTO user_member_in_clubs (members_id, member_in_clubs_id) VALUES (%s, %s)"
    cursor.execute(q, (u_id, club_id))
    connection.commit()

    # create user_trainer_in_clubs 10 percent of users are trainers
    if randint(1, 10) == 1:
        q = "INSERT INTO user_trainer_in_clubs (trainers_id, trainer_in_clubs_id) VALUES (%s, %s)"
        cursor.execute(q, (u_id, club_id))
        connection.commit()
    
    # create user_admin_in_clubs 5 percent of users are admins
    if randint(1, 20) == 1:
        q = "INSERT INTO user_admin_in_clubs (admins_id, admin_in_clubs_id) VALUES (%s, %s)"
        cursor.execute(q, (u_id, club_id))
        connection.commit()

    
if (connection.is_connected()):
            cursor.close()
            connection.close()
    

    




