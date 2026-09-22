cliente=(input("Digite o nome do cliente: "))
renda_mensal =float(input('Digite a renda mensal do cliente: \nLEMBRETE! escreva o salario com "." um exemplo: 4000.00 \n '))
score=int(input(f"Digite o score do cliente {cliente}: "))
restricao= int(input('Digite "0" se o cliente não tiver restrição e "1" caso o cliente tenha restrição: '))

if score>=700 and renda_mensal>=4000.00 and restricao == 0 :
    print(f"Parabéns {cliente}, você tem emprestimo aprovado!")

elif (renda_mensal>=2500.00 and restricao == 0) or (score>=500 or renda_mensal>=6000.00) :
    print(f"Infelizmente não aprovado diretamente, podemos tentar conversar com o gerente!")
else:
    print("Infelizmente não podemos fazer nada, você não tem pontos suficiente para um emprestimo. ")
