import mysql.connector
import os
from dotenv import load_dotenv
from collections import deque

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


# Function to find the crafting chain for an element
def find_crafting_chain_depth(element_id):
    cursor = connection.cursor(dictionary=True)

    # Recursive function to find crafting chain
    def recursive_find_chain(element_id, visited):
        if element_id in [1, 2, 3, 4]:
            return [element_id]
        # Fetch the craft with the lowest depth for the given element
        cursor.execute(
            "SELECT item_1_id, item_2_id FROM crafts WHERE result_id = %s AND depth IS NOT NULL ORDER BY depth ASC LIMIT 1",
            (element_id,)
        )
        craft = cursor.fetchone()
        if craft:
            # Retrieve the ingredients of the craft
            item_1_id, item_2_id = craft['item_1_id'], craft['item_2_id']
            # Recursively find the crafting chain for each ingredient
            if item_1_id not in visited:
                chain_item_1 = recursive_find_chain(item_1_id, visited | {item_1_id})
            else:
                chain_item_1 = []
            if item_2_id not in visited:
                chain_item_2 = recursive_find_chain(item_2_id, visited | {item_2_id})
            else:
                chain_item_2 = []
            return chain_item_1 + chain_item_2
        else:
            # Check if the element is a base element (depth = 0 or ID = 1, 2, 3, 4)
            cursor.execute(
                "SELECT depth FROM elements WHERE id = %s",
                (element_id,)
            )
            element_depth = cursor.fetchone()['depth']
            if element_depth == 0 or element_id in [1, 2, 3, 4]:
                return [element_id]
            else:
                # Handle case where element is not a base element but there is no craft available
                raise ValueError(f"No craft available for element ID {element_id}")

    # Start the recursive search
    crafting_chain = recursive_find_chain(element_id, {element_id})

    return crafting_chain


def find_crafting_chain_depth_iter(element_id):
    cursor = connection.cursor(dictionary=True)
    tree = {element_id : None}


    def get_rec(element_id):
        if element_id in [1,2,3,4]:
            return {}
        cursor.execute(
            "SELECT item_1_id, item_2_id FROM crafts WHERE result_id = %s AND depth IS NOT NULL ORDER BY depth ASC LIMIT 1",
            (element_id,)
        )
        craft = cursor.fetchone()
        if craft:
            return {craft['item_1_id'] : None, craft['item_2_id'] : None}

    def it_nested_dict(d):
        for k,v in d.items():
            if v == None:
                d[k] = get_rec(k)
            elif isinstance(v, dict):
                d[k] = it_nested_dict(v)
        return d

    for i in range(20):
        tree = it_nested_dict(tree)
    return tree

# Example usage
element_id = 2000  # Change this to the desired element ID
crafting_chain = find_crafting_chain_depth_iter(element_id)
if crafting_chain:
    print(f"Shortest crafting chain for element ID {element_id}: {crafting_chain}")
else:
    print(f"No crafting chain found for element ID {element_id}")

# Close the connection
connection.close()
