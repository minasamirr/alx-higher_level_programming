#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select cities with their respective states
    sql_query = """
                SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states ON cities.state_id = states.id
                ORDER BY cities.id
                """
    cursor.execute(sql_query)

    # Fetch all the rows using fetchall() method
    data = cursor.fetchall()

    # Print the result
    for row in data:
        print(row)

    # Disconnect from server
    db.close()
