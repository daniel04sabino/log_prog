

def bubble_sort(lista):
    tamanho=len(lista)
    #for para controlar passadas
    for i in range(tamanho):
        houve_troca=False
        #for para comparar números na lista
        for j in range(0,tamanho -i -1):
            if lista[j] >lista[j+1]:
                #faz a troca direta de valores entre posiçoes vizinhas
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                houve_troca = True

        if not houve_troca:
            break

    return lista

# def insertion_sort(lista):
#     tamanho=len(lista)
#     lista2=[]
#     while True:
#         for j in range(0,tamanho  -1):
#             if lista[j]> lista[j-1]:
#                 lista2.insert(lista[j],lista[j-1])
#             else:
#                 pass
#         if lista[0]> lista[]
#     lista=lista2


pape = [2,4,5,8,0,10]
# bubble_sort(pape)
# insertion_sort(pape)
print(pape)