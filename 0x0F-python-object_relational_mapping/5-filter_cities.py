#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Execute SQL query to select cities of the given state
    sql_query = """
                SELECT GROUP_CONCAT(cities.name ORDER BY cities.id SEPARATOR ', ')
                FROM cities
                JOIN states ON cities.state_id = states.id
                WHERE states.name = %s
                GROUP BY states.name
                """
    cursor.execute(sql_query, (state_name,))

    # Fetch the row using fetchone() method
    data = cursor.fetchone()

    # Print the result
    if data:
        print(data[0])
    else:
        print("")

    # Disconnect from server
    db.close()
