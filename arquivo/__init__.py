from HelloUser.utilidades import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print(f'\033[31mHouve um erro na criação do arquivo.')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def listarArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print(f'\033[31mHouve um erro na listagem do arquivo.')
    else:
        titulo('PESSOAS CADASTRADAS')
        for linha in a:
            dados = linha.split(';')
            dados[1] = dados[1].replace('\n','')
            print(f'{dados[0]:<22}{dados[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')
    except:
        print(f'Houve um erro na abertura do arquivo.')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print(f'Houve um erro no cadastro do cliente.')
        else:
            print(f'\033[34mREGISTRO REALIZADO COM SUCESSO\033[m')
            a.close()
