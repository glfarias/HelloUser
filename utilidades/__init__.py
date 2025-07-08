def linha(tam=30):
    return print(f'\033[34m-' * tam)


def titulo(msg, cor=34, tam=30):
    print(f'\033[{cor}m', end='')
    print(f'-' * tam)
    print(f'{msg.center(tam)}')
    print(f'-' * tam, end='')
    print(f'\033[m')


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except KeyboardInterrupt:
            print(f'\n\033[0;34mO usuário preferiu não digitar.\033[m')
            n = 0
            break
        except:
            print(f'\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        else:
            break
    return n


def leiaStr(msg):
    while True:
        try:
            nome = input(msg).strip().title()
            nome = ' '.join(nome.split())
            if nome == '':
                raise ValueError('O campo nome não deve estar vazio.')
            for char in nome:
                if char.isdigit():
                    raise ValueError('O campo nome não deve conter números.')
                if not (char.isalpha() or char in ' '):
                    raise ValueError('O campo nome não deve conter caracteres especiais.')
        except KeyboardInterrupt:
            print('\n\033[0;34mO usuário preferiu não digitar.\033[m')
            return ''
        except ValueError as x:
            print(f'\033[0;31mERRO! {x}\033[m')
        else:
            return nome