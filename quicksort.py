def quicksort(lista):
    quicksort_recursivo(lista,0,len(lista)-1)
    return lista

def quicksort_recursivo(lista,inicio,fim):
    if fim > inicio:
        indice_pivo = dividir(lista,inicio,fim)
        quicksort_recursivo(lista,inicio,indice_pivo-1)
        quicksort_recursivo(lista,indice_pivo+1,fim)


def dividir(lista,inicio,fim):
    pivo=lista[fim]
    # pivo=lista[inicio]
    # pivo=lista[len(lista)//2] pegario o pivo no meio do vetor
    i = inicio - 1
    for j in range(inicio,fim):
        if lista[j]<= pivo:
            i+=1
            lista[i],lista[j] = lista[j],lista[i]


l=[3,5,6,7,8,9,4,3,2,6,7,8,5]
