from utilidades import *


def menuprincipal():
    # DECLARO A LISTA DE OPÇÕES DE MENU, FAZEMOS DESSA FORMA
    # PARA NO FUTURO POSSIVELMENTE IMPLEMENTAR MAIS OPÇÕES
    funções = ['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema']

    #
    titulo('MENU PRINCIPAL')

    for i, v in enumerate(funções):
        print(f'\033[1;36m{i+1}\033[m - \033[34m{v}')
    linha()

    while True:
        try:
            opção = int(input(f'\033[34m> \033[m'))
        except ValueError:
            print(f'\033[31mERRO! Digite uma opção válida.\033[m')
        else:
            if opção < 1 or opção > 3:
                print(f'\033[31mERRO! Digite uma opção válida.\033[m')
            else:
                break
    return opção
