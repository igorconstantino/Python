file_path = '.\\exercicios\\test.txt'

with open(file_path, 'a+') as file:
    file.write('Hello World!\n')
    file.seek(0, 0)
    print(file.read())
