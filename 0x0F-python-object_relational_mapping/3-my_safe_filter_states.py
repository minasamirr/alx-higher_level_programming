#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states where name matches the provided argument safely
    sql_query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(sql_query, (state_name,))

    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Print the result
    for row in data:
        print(row)

    # Disconnect from server
    db.close()
