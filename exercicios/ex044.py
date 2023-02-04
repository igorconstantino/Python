preco_produto = float(input('Digite o preco do produto: '))
forma_pagamento = input('Digite sua forma de pagamento: ')

if forma_pagamento == 'dinheiro':
    print('Você pagará R${:.2f}'.format(preco_produto - preco_produto * 0.1))
elif forma_pagamento == 'cartão':
    print('Você pagará R${:.2f}'.format(preco_produto - preco_produto * 0.05))
elif forma_pagamento == '2x cartão':
    print('Você pagará R${:.2f}'.format(preco_produto))
elif forma_pagamento == '3x ou mais':
    print('Você pagará R${:.2f}'.format(preco_produto + preco_produto * 0.2))
