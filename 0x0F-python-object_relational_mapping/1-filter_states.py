#!/usr/bin/python3
"""
Script to list all states with names starting with 'N' from a MySQL database.

Usage: ./1-filter_states.py username password database

Arguments:
    username: MySQL username
    password: MySQL password
    database: Name of the database containing the states table

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
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Get arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

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

    # Execute the query
    try:
        cursor.execute(
                "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
        results = cursor.fetchall()
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    # Close cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
