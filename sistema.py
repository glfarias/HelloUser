from time import sleep
from menu import *
from arquivo import *
from utilidades import *

# VERIFICO SE O ARQUIVO EXISTE
# SE NÃO EXISTE, CRIA O ARQUIVO
arq = 'database.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)


# LOOP INFINITO, CHAMANDO O MENU PRINCIPAL
# DENTRO DE MENUPRINCIPAL É VALIDADA PRA QUE A RESPOSTA SEJA 1, 2 OU 3
while True:
    x = menuprincipal()
    if x == 1:
        listarArquivo(arq)
        sleep(1.5)
        print()
    if x == 2:
        titulo('NOVO CADASTRO')
        nome = leiaStr('Nome: ')
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        sleep(1.5)
    if x == 3:
        titulo('FINALIZANDO SISTEMA', cor=33)
        sleep(1.5)
        break