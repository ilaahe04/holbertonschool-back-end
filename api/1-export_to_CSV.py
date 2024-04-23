#!/usr/bin/python3

"""
    export data in the CSV format.
"""


if __name__ == "__main__":

    import csv
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    username = requests.get(f"https://jsonplaceholder.\
typicode.com/users/{argv[1]}").json().get('username')

    todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()

    writer = csv.writer(open(f'{argv[1]}.csv', 'w'), quoting=csv.QUOTE_ALL)

    for todo in todos:
        writer.writerow([todo.get('userId'), username,
                         todo.get('completed'), todo.get('title')])
