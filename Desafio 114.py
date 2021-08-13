
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[1;31mFALHA DE CONEXÃO/URL INEXISTENTE\033[m')
else:
    print('\033[1;32mCONEXÃO PERFEITA, ACESSANDO O SITE COM SUCESSO!\033[m')
