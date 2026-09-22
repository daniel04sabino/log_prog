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

#Botão

def gameplay():
 
 
 botaoPedra.place(x=295,y=300)
 botaoTesoura.place(x=495,y=300)
 botaoPapel.place(x=395,y=300)
 

botao_jxj=Button(janela,text="Jogador X Jogador ",command=gameplay)
botao_jxj.place(x=300,y=150)

botao_cpu=Button(janela,text="Jogador X CPU ",command=gameplay)
botao_cpu.place(x=450,y=150)



def botaoPedra():
    print("Pedra")
botaoPedra=Button(
    janela,image=imgPedra,command=botaoPedra,borderwidth=0,border=0
)

def botaoPapel():
    print("Papel")
botaoPapel=Button(
    janela,image=imgPapel,command=botaoPapel,borderwidth=0
)

def botaoTesoura():
    print("Tesoura")
botaoTesoura=Button(
    janela,image=imgTesoura,command=botaoTesoura,borderwidth=0
)

# if jogador1 == jogador2 :
#    print(f'Tivemos um empate! ')
# elif jogador1 == "Pedra" and jogador2 == "Tesoura": 
#  print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

# elif jogador1 == "Pedra" and jogador2 == "Papel": 
#  print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

# elif jogador1 == "Papel" and jogador2 == "Tesoura": 
#  print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

# elif jogador1 == "Tesoura" and jogador2 == "Pedra": 
#  print(f"Jogador 2 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

# elif jogador1 == "Tesoura" and jogador2 == "Papel": 
#  print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")

# elif jogador1 == "Papel" and jogador2 == "Pedra": 
#  print(f"Jogador 1 Venceu. \nJogador 1 escolheu {jogador1} e jogador escolheu {jogador2}.  ")



janela.mainloop()