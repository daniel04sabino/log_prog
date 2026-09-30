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
jogadas=(pedra,papel,tesoura)
jogador_x_jogador=(False)
#Botão
bigmente=()
jogador=()
jogador2=()

def escolher_jogador(escolha):
    global jogador
    jogador = escolha
    print(f"Jogador escolheu: {jogador}")

def escolher_jogador(escolha):
    global jogador2
    jogador2 = escolha
    print(f"Jogador escolheu: {jogador2}")

def gameplay():
    botaoPedra=Button(
    janela,image=imgPedra,command=lambda: escolher_jogador(pedra),borderwidth=0,border=0)
    botaoPedra.place(x=295,y=300)
    
    botaoTesoura=Button(
    janela,image=imgTesoura,command=lambda:escolher_jogador(tesoura),borderwidth=0)
    botaoTesoura.place(x=495,y=300)
    
    botaoPapel=Button(janela,image=imgPapel,command=lambda: escolher_jogador(papel),borderwidth=0)
    botaoPapel.place(x=395,y=300)
    bigmente = random.choice(jogadas)
    

def x1():
    Jog1=Label(janela,text='Jogador 1')
    Jog1.place(x=400,y=100)

    botaoPedra=Button(
    janela,image=imgPedra,command=lambda: escolher_jogador(pedra),borderwidth=0,border=0)
    botaoPedra.place(x=295,y=300)
        
    botaoTesoura=Button(
    janela,image=imgTesoura,command=lambda:escolher_jogador(tesoura),borderwidth=0)
    botaoTesoura.place(x=495,y=300)
        
    botaoPapel=Button(janela,image=imgPapel,command=lambda: escolher_jogador(papel),borderwidth=0)
    botaoPapel.place(x=395,y=300)
    
    return x1_2

def x1_2():
    Jog1=Label(janela,text='Jogador 2')
    Jog1.place(x=400,y=100)

    botaoPedra=Button(
    janela,image=imgPedra,command=lambda jogador2:pedra,borderwidth=0,border=0)
    botaoPedra.place(x=295,y=300)
        
    botaoTesoura=Button(
    janela,image=imgTesoura,command=lambda jogador2:tesoura,borderwidth=0)
    botaoTesoura.place(x=495,y=300)
        
    botaoPapel=Button(janela,image=imgPapel,command=lambda jogador2:papel,borderwidth=0)
    botaoPapel.place(x=395,y=300)


# def Bigmen():
#    random.choice(jogadas)
#    return bigmente

 

botao_jxj=Button(janela,text="Jogador X Jogador ",command=x1)
botao_jxj.place(x=300,y=150)

botao_cpu=Button(janela,text="Jogador X CPU ",command=gameplay)
botao_cpu.place(x=450,y=150)



def botaoPedra():
    Button(
    janela,image=imgPedra,command=lambda:pedra,borderwidth=0,border=0)
    botaoPedra.place(x=295,y=300)
    # jogador=(pedra)
    return jogador(pedra)

def botaoPapel():
    Button(janela,image=imgPapel,command=lambda jogador:papel,borderwidth=0)
    botaoPapel.place(x=395,y=300)
    # jogador=(papel)
    return jogador(papel)

def botaoTesoura():
    Button(
    janela,image=imgTesoura,command=lambda:tesoura,borderwidth=0)
    botaoTesoura.place(x=495,y=300)
     # jogador=(tesoura)
    return jogador(tesoura)


if jogador_x_jogador:
    if jogador == jogador2 :
        print(f'Tivemos um empate! ')

    elif jogador == pedra and jogador2 == tesoura: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == pedra and jogador2 == papel: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == papel and jogador2 == tesoura: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == tesoura and jogador2 == pedra: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == tesoura and jogador2 == papel: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")

    elif jogador == papel and jogador2 == pedra: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {jogador2}.  ")
else:
    if jogador == bigmente :
        print(f'Tivemos um empate! ')
    elif jogador == pedra and bigmente == tesoura: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

    elif jogador == pedra and bigmente == papel: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

    elif jogador == papel and bigmente == tesoura: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

    elif jogador == tesoura and bigmente == pedra: 
        print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

    elif jogador == tesoura and bigmente == papel: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")

    elif jogador == papel and bigmente == pedra: 
        print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador} e jogador escolheu {bigmente}.  ")


janela.mainloop()