#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select states starting with 'N' sorted by id
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Print the result
    for row in data:
        print(row)

    # Disconnect from server
    db.close()
