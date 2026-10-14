#fila_tarefas contendo: "Backup", "Envio de Logs","Limpeza de Cache".

fila_tarefas=['Backup', 'Envio de Logs','Limpeza de Cache']
#print(fila_tarefas)
fila_tarefas.append('Atualização de Dependências')
#print(fila_tarefas)
fila_tarefas.insert(0,'Correção de Bug Crítico')
#print(fila_tarefas)
fila_tarefas.remove('Limpeza de Cache')
#print(fila_tarefas)
print(len(fila_tarefas))
print(fila_tarefas[0])
print(fila_tarefas[-1])
