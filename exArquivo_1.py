alunos=[]
with open('Alunos.txt', 'w', encoding="utf-8")as arquivo:
    for i in range(0,3):
        nome= input('Digite seu nome: ')
        # idade= int(input('Digite sua idade: '))
        # turma= input('Digite a turma: ')
        # alunos.append(nome)
        arquivo.write(nome+'\n')
        




