import mysql.connector

# Connect to your MySQL server
conn = mysql.connector.connect(
    host='localhost',
    user='ruser',
    password='root',
    database='lolrankings'
)

# Create a MySQL cursor
cursor = conn.cursor()

# Read data from the text file
file_path = 'rankings.txt'

with open(file_path, 'r') as file:
    lines = file.readlines()

# Iterate over the lines and insert data into the database
for line in lines:
    data = eval(line)
    
    # Extracting required values
    name, role, stat_name, stat_num, rank = data
    stat_num = float(stat_num.replace('.', '').replace(',', '.'))  # Convert to float, removing commas
    rank = int(rank.split('/')[0].strip())  # Extract the number before '/'
    stat_name = stat_name.rstrip(':')  # Remove trailing ':'

    # Insert data into the database
    query = "INSERT INTO data (name, role, stat_name, stat_num, `rank`) VALUES (%s, %s, %s, %s, %s)"
    values = (name, role, stat_name, stat_num, rank)

    cursor.execute(query, values)

# Commit the changes
conn.commit()

# Close the cursor and connection
cursor.close()
conn.close()
