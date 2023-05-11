print("Valor Exato: ")
Ve = float(input())

print("Valor Aproximado: ")
Va = float(input())

Ea = abs(Ve - Va)
Er = Ea / Ve * 100

print(f"O erro absoluto é {Ea} e o erro relativo é {Er}")
