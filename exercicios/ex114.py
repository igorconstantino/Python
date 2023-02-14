from urllib import request

try:
    site = request.urlopen('http://www.pudim.com.br')
except:
    print('Site não está acessível no momento')
else:
    print('Site acessível no momento')
