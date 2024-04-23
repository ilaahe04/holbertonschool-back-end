#!/usr/bin/python3

"""
    export data in the CSV format.
"""


if __name__ == "__main__":

    import json
    import requests


    dict_n = {}

    user_list = requests.get(f"https://jsonplaceholder.\
typicode.com/users/").json()
    
    for user in user_list:
        todos = requests.get(f"https://jsonplaceholder.typicode.\
com/todos?userId={user.get('id')}").json()
    list_n = []
    for todo in todos:
        list_n.append({'username': user.get('username'),
                       :wq'task': todo.get('title'),
                             'completed': todo.get('completed')})
    dict_n[user.get('id')] = list_n
    json.dump(dict_n, open(f"todo_all_employees.json", "w"))
