notas=[]
acima_da_media=[]
for i in range(0,4):
    av= float(input('Digite sua nota: '))
    notas.append(av)

media=sum(notas)/(len(notas))
for nota in notas:
    if nota>media:
        acima_da_media.append(nota)

print(f'Essa foi a média: {media}\nE essas são as notas que ficaram acima da média:{acima_da_media} ') 