import random
print("Rodada 1")
jogadas= int(input('Descubra o número entre 0 e 50:\n '))
computador=random.randint(0,50)
jogou=1
pontos=300
lose=25

if jogadas==computador:
    print(f'Parabens! Você acertou.\nVocê acertou e ganhou {pontos} pontos!')

    if jogadas > computador:
     print("O número é maior que o esperado: ")
    elif jogadas < computador:
     print("O número é menor que o esperado: ")
elif jogadas!=computador:
    while(jogou <5):
     #  print("Rodada 1")
     jogou+=1
     pontos=pontos-lose
     jogadas= int(input('Descubra o número entre 0 e 50: '))
     if jogadas < computador:
        print("\nO número é maior que o esperado: ")
     elif jogadas > computador:
        print("\nO número é menor que o esperado: ")
        # print(f"essa é a senha '{computador}': {pontos}")
     elif jogadas==computador:
        print(f'Parabens! Você acertou.\nVocê acertou e ganhou {pontos} pontos! ')
        break
        


# print("Segunda Rodada, agora vale 200\n")

if jogadas != computador:
    jogou=0
    print("Segunda Rodada, agora vale 200\n")
    while(jogou <5):
        jogou+=1
        pontos=pontos-lose
        jogadas= int(input('Descubra o número entre 0 e 50: '))
            # print(f"essa é a senha '{computador}': {pontos}")
        if jogadas < computador:
            print("\nO número é maior que o esperado: ")
        elif jogadas > computador:
            print("\nO número é menor que o esperado: ")
        elif jogadas==computador:
            print(f'Parabens! Você acertou.\nVocê acertou e ganhou {pontos} pontos! ')
            break


if jogadas != computador:  
 print("Terceira Rodada, agora vale 100\n")
 jogou=0
 while(jogou <5):
        # print("Terceira Rodada, agora vale 100\n")
        jogou+=1
        pontos=pontos-lose
        jogadas= int(input('Descubra o número entre 0 e 50: '))
        # print(f"essa é a senha '{computador}':{pontos} ")
        if jogadas < computador:
                print("\nO número é maior que o esperado: ")
        elif jogadas > computador:
                print("\nO número é menor que o esperado: ")
        elif jogadas==computador:
                print(f'Parabens! Você acertou.\nVocê acertou e ganhou {pontos} pontos!')
                break
        elif jogou ==5 and jogadas!=computador:
         print("Infelizmente você não acertou")
             