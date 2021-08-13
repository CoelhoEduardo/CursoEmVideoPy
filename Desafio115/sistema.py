
from time import sleep
from Desafio115.lib.Interface import *
from Desafio115.lib.Arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    opcao = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if opcao == 1:
        #Opção de listar o conteúdo de um arquivo!
        lerArquivo(arq)
    elif opcao == 2:
        #Opção de cadastrar uma nova pessoa.
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        #Opção para Sair do sistema
        cabecalho('SAINDO DO SISTEMA... ATÉ LOGO'.center(50))
        break
    else:
        print('\033[1;31mERRO: Digite uma opção válida\033[m')
    sleep(1)
