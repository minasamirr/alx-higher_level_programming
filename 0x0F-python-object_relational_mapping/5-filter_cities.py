#!/usr/bin/python3
"""
Script to list all cities of a given state from a MySQL database.

Usage: ./5-filter_cities.py username password database state_name

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the database containing the cities table
    state_name: Name of the state to search for

Requirements:
    - MySQLdb module
"""

import MySQLdb
import sys


def main():
    """
    Main function to execute the script.
    """
    # Check if all required arguments are provided
    if len(sys.argv) != 5:
        print("Usage: {} username password database state_name".format(
            sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve cities of the given state
    try:
        query = "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') FROM cities JOIN states ON cities.state_id = states.id WHERE states.name = %s ORDER BY cities.id ASC;"
        cursor.execute(query, (state_name,))
        result = cursor.fetchone()
        if result[0]:
            print(result[0])
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
