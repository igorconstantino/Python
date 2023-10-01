import todo_list
import json


path = '.\\exercicios\\todo.json'

with open(path, 'w') as file:
    json.dump(todo_list.todo, file)

with open(path, 'r') as file:
    print(json.load(file))
