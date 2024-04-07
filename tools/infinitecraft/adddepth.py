import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")
MYSQL_PORT = os.getenv("MYSQL_PORT")

# Connect to the database
connection = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE,
    port=MYSQL_PORT
)

def add_depth_crafts():
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM crafts")
    c = 0
    for row in cursor.fetchall():
        c+= 1
        r_id  = row[0]
        i_1_id = row[1]
        i_2_id = row[2]

        # check if i_1 has depth
        cursor.execute("SELECT depth FROM elements WHERE id = %s", (i_1_id,))
        
        depth_1 = cursor.fetchone()[0]
        if depth_1 is None:
            continue

        cursor.execute("SELECT depth FROM elements WHERE id = %s", (i_2_id,))
        depth_2 = cursor.fetchone()[0]
        if depth_2 is None:
            continue

        if i_1_id == i_2_id:
            if i_1_id == r_id:
                depth =  depth_1 + depth_2 + 1
            else:
                depth = max(depth_1, depth_2) + 1
        else:
            depth =  depth_1 + depth_2 + 1

        cursor.execute("UPDATE crafts SET depth = %s WHERE result_id = %s AND item_1_id = %s AND item_2_id = %s", (depth, r_id, i_1_id, i_2_id))
        if c % 100 == 0:
            print("Updated %s crafts" % c)
            print("Updated craft %s" % r_id)
        connection.commit()

def add_depth_elements():
    
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM elements")
    for row in cursor.fetchall():
        e_id = row[0]
        if e_id in [1,2,3,4]:
            continue
        # get all recipes where result_id is e_id and order them by their depth
        cursor.execute("SELECT * FROM crafts WHERE result_id = %s AND depth IS NOT NULL ORDER BY depth ASC LIMIT 1",(e_id,))
        res = cursor.fetchone()
        if res is None:
            continue
        depth = res[3]
        cursor.execute("UPDATE elements SET depth = %s WHERE id = %s", (depth, e_id))
        print("Updated element %s" % e_id)
        connection.commit()


if __name__ == "__main__":
    while True:
        add_depth_crafts()
        add_depth_elements()

# check if i_2 has depth