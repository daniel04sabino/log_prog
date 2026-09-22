# pedra=("Pedra")
# papel=("Papel")
# tesoura=("Tesoura")
# start = (input(f'Jogo simples, pode ser apenas: pedra, papel e tesoura. \n Se você entendeu digite "Ok" '))
# start2 =() 

# if start=="ok":
jogador1 = (input(f"Jogador 1, Digite qual é sua escolha \n pode ser apenas: pedra, papel e tesoura "))
    # start2 = (input('Agora, Jogador 2, digite "Ok" para começar. '))

# elif start2 == "ok":
jogador2 = (input(f"Jogador 2, Digite qual é sua escolha \n pode ser apenas: pedra, papel e tesoura. "))

# else:
#     print("digite Ok para começar. ")

print("Ok, agora vamos descobri quem ganhou. ")
if jogador1 == jogador2 :
   print(f'Tivemos um empate! ')
elif jogador1 == "Pedra" and jogador2 == "Tesoura": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

elif jogador1 == "Pedra" and jogador2 == "Papel": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

elif jogador1 == "Papel" and jogador2 == "Tesoura": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

elif jogador1 == "Tesoura" and jogador2 == "Pedra": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

elif jogador1 == "Tesoura" and jogador2 == "Papel": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

elif jogador1 == "Papel" and jogador2 == "Pedra": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")