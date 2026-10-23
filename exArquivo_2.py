with open('Alunos.txt', 'r', encoding='utf-8') as arquivo :
    num=0
    for linha in arquivo:
        num+=1
        # nome = linha.strip(linha)
        # print(f'Nº {linha} | Nome: {nome}')
        print(f'Nº: {num} | {linha}')
