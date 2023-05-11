
base = int(input('Digite a base: '))
digitos = int(input('Digite o número de dígitos: '))
expoente = int(input('Digite o expoente: '))
num = float(input('Digite um número: '))

def ponto_flutuante(base, digitos, expoente, numero):
    if numero == 0:
        return 0
    else:
        sinal = "+"
        if numero < 0:
            sinal = "-"
            numero = -numero

        expoenteCalculado = 0
        while numero >= base:
            numero /= base
            expoenteCalculado += 1
        while numero < 0.1:
            numero *= base
            expoenteCalculado -= 1

        if expoenteCalculado < -expoente:
            expoenteCalculado = -expoente
        elif expoenteCalculado > expoente:
            expoenteCalculado = expoente
        numero = round(numero, digitos)

        return f"{sinal} {numero} * {base} ^ {expoenteCalculado}"
    
print(ponto_flutuante(base, digitos, expoente, num))