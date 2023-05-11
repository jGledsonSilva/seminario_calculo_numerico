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

base = -1
while base <= 0:
  try:
    base = int(input('Digite a base: '))
    if base <= 0:
      raise ValueError('A base deve ser maior que zero.')
  except ValueError as e:
    print(f'Erro: {e}')
    base = -1

digitos = -1
while digitos <= 0:
  try:
    digitos = int(input('Digite o número de dígitos: '))
    if digitos <= 0:
      raise ValueError('O número de dígitos deve ser maior que zero.')
  except ValueError as e:
    print(f'Erro: {e}')
    digitos = -1

expoente = -1
while expoente <= 0:
  try:
    expoente = int(input('Digite o expoente de precisão: '))
    if digitos <= 0:
      raise ValueError('O expoente de precisão deve ser maior que zero.')
  except ValueError as e:
    print(f'Erro: {e}')
    digitos = -1

num = None
while num == None:
  try:
    num = float(input('Digite um número: '))
  except ValueError as e:
    print(f'Erro: {e}')
    num = None
    
print(ponto_flutuante(base, digitos, expoente, num))
