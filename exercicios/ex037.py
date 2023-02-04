num = int(input('Digite um número: '))

print('Escreva para qual base deseja converter')
print("""(1) - Binária
(2) - Octal
(3) - Hexadecimal """)

opcao = int(input())

if opcao == 1:
    print(bin(num)[2:])
elif opcao == 2:
    print(oct(num)[2:])
elif opcao == 3:
    print(hex(num)[2:])
else:
    print('Digite um número válido!')
