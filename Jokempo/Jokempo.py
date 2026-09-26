#Tela
from tkinter import *
import random


janela= Tk()
janela.title("Jokenpo")
janela.geometry("900x600")
icon= PhotoImage(file="img/Icon.png")
janela.iconphoto(True,icon)
fundo= PhotoImage(file="img/fundo2.png")
tela=Label(janela,image=fundo)
tela.place(x=0,y=0)

#Imagens
imgPedra=PhotoImage(file="img/Pedra.png",)
imgPapel=PhotoImage(file="img/Papel.png")
imgTesoura=PhotoImage(file="img/Tesoura.png")


#textos


label= Label(janela,text="Pedra, Papel e Tesoura")
label.place(x=400,y=56)


pedra=('pedra')
papel=('papel')
tesoura=('tesoura')
jogadas=('pedra','papel','tesoura')
jogador_x_jogador=(False)
#Botão
bigmente=()
jogador=()
jogador2=()
def gameplay():
    botaoPedra.place(x=295,y=300)
    botaoTesoura.place(x=495,y=300)
    botaoPapel.place(x=395,y=300)
    bigmente= random.choice(jogadas)
    

def x1():
    Jog1=Label(janela,text='Jogador 1',command=jogador_x_jogador)
    Jog1.place(x=400,y=56)
    botaoPedra.place(x=295,y=300)
    botaoTesoura.place(x=495,y=300)
    botaoPapel.place(x=395,y=300)
    # jogador_x_jogador=(True)




# def Bigmen():
#    random.choice(jogadas)
#    return bigmente

 

botao_jxj=Button(janela,text="Jogador X Jogador ",command=x1)
botao_jxj.place(x=300,y=150)

botao_cpu=Button(janela,text="Jogador X CPU ",command=gameplay)
botao_cpu.place(x=450,y=150)



def botaoPedra():
    botaoPedra=Button(
    janela,image=imgPedra,command=botaoPedra,borderwidth=0,border=0)
    # jogador=(pedra)
    # return jogador

def botaoPapel():
    botaoPapel=Button(janela,image=imgPapel,command=botaoPapel,borderwidth=0)
    jogador=(papel)
    return jogador

def botaoTesoura():
    botaoTesoura=Button(
    janela,image=imgTesoura,command=botaoTesoura,borderwidth=0)
    jogador=(tesoura)
    return jogador


if jogador_x_jogador:
    if jogador == jogador2 :
        print(f'Tivemos um empate! ')

    elif jogador == "Pedra" and jogador2 == "Tesoura": 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == "Pedra" and jogador2 == "Papel": 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == "Papel" and jogador2 == "Tesoura": 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == "Tesoura" and jogador2 == "Pedra": 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == "Tesoura" and jogador2 == "Papel": 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == "Papel" and jogador2 == "Pedra": 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")
 
elif jogador == bigmente :
   print(f'Tivemos um empate! ')
elif jogador == "Pedra" and bigmente == "Tesoura": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

elif jogador == "Pedra" and bigmente == "Papel": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

elif jogador == "Papel" and bigmente == "Tesoura": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

elif jogador == "Tesoura" and bigmente == "Pedra": 
 print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

elif jogador == "Tesoura" and bigmente == "Papel": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

elif jogador == "Papel" and bigmente == "Pedra": 
 print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")


janela.mainloop()