from dotenv import load_dotenv
import mysql.connector
import os


# Load environment variables from .env file
load_dotenv()

# Read MySQL connection details from environment variables
MYSQL_HOST = os.getenv("MYSQL_HOST")
MYSQL_USER = os.getenv("MYSQL_USER")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

# Connect to the database
conn = mysql.connector.connect(
    host=MYSQL_HOST,
    user=MYSQL_USER,
    password=MYSQL_PASSWORD,
    database=MYSQL_DATABASE
)

if __name__ == "__main__":
    cursor = conn.cursor()

    """
    # remove all depths > 20
    cursor.execute(
        "Update crafts SET depth = NULL WHERE depth > 20"
    )
    conn.commit()
    cursor.execute(
        "Update elements SET depth = NULL WHERE depth > 20"
    )
    conn.commit()
    """




    # get all element ids
    q = "select id,name from elements"
    cursor.execute(q)
    ids = cursor.fetchall()

    for i in ids:
        element_id = i[0]
        #

        # get the craft with the lowest depth for every element

        cursor.execute(
            "SELECT item_1_id, item_2_id FROM crafts WHERE result_id = %s AND depth IS NOT NULL ORDER BY depth ASC LIMIT 1",
            (element_id,)
        )

        craft = cursor.fetchone()
        if craft:
            if craft[0] == element_id or craft[1] == element_id:
                print(f"element {element_id} is not verified", i[1])
                # delete all crafts containing ths element

                cursor.execute(
                    "DELETE FROM crafts WHERE result_id = %s OR item_1_id = %s OR item_2_id = %s",
                    (element_id, element_id, element_id)
                )
                conn.commit()

                cursor.execute(
                    "UPDATE elements SET depth = NULL WHERE id = %s",
                    (element_id, ) 
                )
                conn.commit()
                




    conn.close()
