#!/usr/bin/python3

"""
    export data in the CSV format.
"""


if __name__ == "__main__":

    import json
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    dict_n = {}
    list_n = []

    username = requests.get(f"https://jsonplaceholder.\
typicode.com/users/{argv[1]}").json().get('username')

    todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={argv[1]}").json()

    for todo in todos:
        list_n.append({'task': todo.get('title'),
                       'completed': todo.get('completed'),
                       'username': username})
    dict_n[str(argv[1])] = list_n
    json.dump(dict_n, open(f"{argv[1]}.json", "w"))
