fibonacci = [0, 1]
i = 2

num_termos = int(input('Digite o número de termos que você quer mostrar da sequência de Fibonacci: '))

while i < num_termos:
    soma = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(soma)
    i += 1

print(fibonacci)
