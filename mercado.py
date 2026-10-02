#mercado
total=float()
cliente=[]
compras=float()
fim_do_cliente=(False)

nome= input('Nome do cliente: ')
while fim_do_cliente==False:
    
    compra= float(input('Digite o valor da compra: '))
    
    compras+=compra
    if compra == -1:
        nome=nome
        compras+=1
        cliente.append([nome,compras])
        total+=compras
        print('Fim da compra do cliente: ')
        nome= input('Nome do cliente: ')
        compras=0       

    elif compra==0:
        nome=nome
        compras+=compra
        cliente.append([nome,compras])
        total+=compras
        fim_do_cliente=True
        
        print(f'O faturamento do dia foi: R${total}')
        for i in range(0,len(cliente)):
            print(f'Cliente: {cliente[i][0]} | Compra: R${cliente[i][1]} ')
        break




    

