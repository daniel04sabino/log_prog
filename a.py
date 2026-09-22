from tkinter import *

janela = Tk()

def abrir_jogo():
    botao_menu.place_forget()

    botao_pedra.place(x=250, y=300)
    botao_papel.place(x=350, y=300)
    botao_tesoura.place(x=450, y=300)


botao_menu = Button(
    janela,
    text="Jogador x Jogador",
    command=abrir_jogo
)
botao_menu.place(x=300, y=150)


botao_pedra = Button(janela, text="Pedra")
botao_papel = Button(janela, text="Papel")
botao_tesoura = Button(janela, text="Tesoura")

janela.mainloop()