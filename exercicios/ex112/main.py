from utils import moeda as md
from utils import dado as dd

valor = dd.leia_dinheiro('Digite o valor: ')
md.resumo(valor, 10, 10)
