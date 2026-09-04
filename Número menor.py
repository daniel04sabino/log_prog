# Como achar o menor valor entre dois números


# Passo 1 -> Ter 2 números
Numero1 = int(input("Digite o Primeiro número: "))
Numero2 = int(input("Digite o Segundo número: "))

# Passo 2 -> testar Condicional
if Numero1 == Numero2:
    print(f"O número {Numero1} é igual o número {Numero2} ")
elif Numero1 < Numero2:
 print(f"O número {Numero1} é menor do que o número {Numero2}")

else: print(f"O número {Numero2} é menor do que o número {Numero1}")
