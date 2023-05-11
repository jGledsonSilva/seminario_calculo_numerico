import os
List = []

def menu():
    print('Converter um número decimal para binário ou binário para decimal')
    print('Digite 1 para converter para binário')
    print('Digite 2 para converter para decimal')
    print('Digite 3 para sair\n')

def valor():
    while True:
        try:
            deci = int(input('\nDigite um número:'))
            break
        except ValueError:
            print('Digite um número válido')
    return deci

def conv_decimal(valor):
    num = valor
    soma = 0
    Listbin = list(str(valor))
    Listbin.reverse()
    for i in range(len(Listbin)):
        soma += int(Listbin[i]) * 2 ** i
    print(f'\nO número {num} em decimal é {soma}\n\n')

def conv_binario(valor, divisao=1):
    num = valor
    while divisao >= 1:
        resto = valor % 2
        divisao = valor // 2
        valor = divisao
        List.append(resto)
    List.reverse()
    valor_binario = "".join(map(str, List))
    print(f'\nO número {num} em binário é {valor_binario}\n\n')
        
while True:
    try:
        menu()
        n = int(input('Escolha as opções:'))
        match n:
            case 1:
                numero = valor()
                conv_binario(numero)
                continua = input('Deseja continuar? [S/N]')
                if continua in 'Nn':
                    break
                elif continua in 'Ss':
                    os.system("cls")
            case 2:
                numero = valor()
                conv_decimal(numero)
                continua = input('Deseja continuar? [S/N]')
                if continua in 'Nn':
                    break
                elif continua in 'Ss':
                    os.system("cls")
            case 3:
                print('Saindo...')
                break
    except ValueError:
        print('\nOpção inválida\nTente novamente\n\n')
