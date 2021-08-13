
def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print(f'\033[1;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return n

def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print(f'\033[1;31mERRO: por favor digite um número real válido\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\033[1;31mUsuário preferiu não digitar esse número\033[m')
            return 0
        else:
            return r


n = leiaInt('Digite um inteiro: ')
r = leiaFloat('Digite um Real: ')
print(f'\033[1;33mValor Inteiro: {n}\033[m \n\033[1;34mValor Real: {r}\033[m')

