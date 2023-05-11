
base = int(input('Digite a base: '))
digitos = int(input('Digite o número de dígitos: '))
menorExpoente = int(input('Digite o menor expoente: '))
maiorExpoente = int(input('Digite o maior expoente: '))
num = float(input('Digite um número: '))

def ponto_flutuante(base, digitos, menorExpoente, maiorExpoente, num):
    if num == 0:
        return 0
    else:
        sinal = "+"
        if num < 0:
            sinal = "-"
            num = -num
        expoente = 0

        if num >= base or num < 1:
            while num >= base:
                num /= base
                expoente += 1
            while num < 1:
                num *= base
                expoente -= 1
            num /= base
            expoente += 1

        if expoente < menorExpoente:
            expoente = menorExpoente
        elif expoente > maiorExpoente:
            expoente = maiorExpoente
        num = round(num, digitos)
        return f"{sinal} {num} * {base} ^ {expoente}"
    
print(ponto_flutuante(base, digitos, menorExpoente, maiorExpoente, num))