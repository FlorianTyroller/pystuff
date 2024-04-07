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


def find_crafting_chain_depth_iter(element_id, max_iters = 20):
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

    for i in range(max_iters):
        tree = it_nested_dict(tree)
    return tree


def print_crafting_chain(chain, prefix='', depth=0):
    if depth == 0:
        print("Crafting chain:")
    
    for item, recipe in chain.items():
        print(f"{prefix}{item}:")
        if isinstance(recipe, dict):
            # If the recipe is a dictionary, recursively print it
            print_crafting_chain(recipe, prefix + '  ', depth + 1)
        else:
            # If the recipe is not a dictionary, it's a base element
            print(f"{prefix}  Base element")
    
    if depth == 0:
        print("End of crafting chain")

def get_crafting_chain_depth(chain):
    max_depth = 0

    for recipe in chain.values():
        if isinstance(recipe, dict):
            # If the value is a dictionary, recursively calculate the depth
            depth = get_crafting_chain_depth(recipe) + 1
            if depth > max_depth:
                max_depth = depth

    return max_depth


if __name__ == "__main__":
    cursor = connection.cursor()
    q = "select id from elements"
    max_iterations = 100
    cursor.execute(q)

    res = cursor.fetchall()

    for i, in res:
        
        ch = find_crafting_chain_depth_iter(i, max_iters = max_iterations)
        d = get_crafting_chain_depth(ch)
        if i % 100 == 0:
            print(i, d)
        if d > 20:
            print(ch)
            break

    