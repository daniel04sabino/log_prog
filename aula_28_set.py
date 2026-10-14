pythonemails_brutos=['ana@empresa.com','carlos@provedor.com','ana@empresa.com','beatriz@servico.com','carlos@provedor.com','daniel@tech.com']

email_unicos = set(pythonemails_brutos)
print(email_unicos)

email_unicos.add('marcos@tech.com')
print('carlos@provedor.com' in email_unicos)
print(len(email_unicos))