print('Olá, esse é um sistema para segurança do maquinário!\n ')
cargo=input('Digite seu Cargo na empresa. \n').lower
cargos=['operador','supervisor']
if cargo not in cargos :
    print(f'Você digitou um cargo errado, exemplos {cargos}. ')
else:
 print('Acesso Bloqueado!')

 hora_atual=int(input('Digite a hora atual. \n"Apenas 0 a 23."\n '))
 hora_de_servico= hora_atual >=8 and hora_atual<=17


 chave_emergencia= input('Você está com a chave de emergencia? \n Use "Y" ou "N"').lower
 if chave_emergencia== "y":
     chave_emergencia= True

 elif chave_emergencia:
     print('Acesso Aprovado! ')

 elif cargo =='supervisor':
     print('Acesso Aprovado! ')

 elif cargo=='operador' and hora_de_servico == True:
     print('Acesso Aprovado! ')
 else:
     print('Acesso Bloqueado!')