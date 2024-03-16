#!/usr/bin/python3
# Connect to MySQL server
# Create a cursor object using cursor() method
# Execute SQL query to select all states sorted by id
# Fetch all the rows using fetchall() method
# Print the result
# Disconnect from server
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    data = cursor.fetchall()
    for row in data:
        print(row)
    db.close()
