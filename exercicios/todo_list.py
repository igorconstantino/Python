todo = []
todo_aux = []

def listar(lista):
    if not lista:
        return
    
    print('TAREFAS:')
    for i, item in enumerate(lista):
        print(f'{i}) {item}')


while True:

    print("""\n\nDigite a opcão desejada ou uma tarefa a ser listada:
(1) - Listar
(2) - Desfazer
(3) - Refazer      
(4) - Sair \n""")

    op = input()

    if op == '1':
        listar(todo)

    elif op == '2':
        if len(todo) != 0:
            todo_aux.append(todo.pop())
        else:
            print('Não há itens a serem removidos!')

        listar(todo)

    elif op == '3':  
        todo.append(todo_aux[-1])
        todo_aux.pop(-1)

        listar(todo)

    elif op == '4':
        print('Obrigado por utilizar nosso programa!')
        break

    else:
        todo.append(op.capitalize())
