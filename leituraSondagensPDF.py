import tabula

lista_tabelas = tabula.read_pdf('SP-37.pdf', pages='all')
print(len(lista_tabelas))

for tabela in lista_tabelas:
    print(tabela)