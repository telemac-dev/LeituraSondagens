import tabula
import pandas as pd

lista_tabelas = tabula.read_pdf('RD_VTaruma_all.pdf', pages='all')
print(len(lista_tabelas))

for tabela in lista_tabelas:

    # Cabecalho com os dados do pdf
    cabecalho = tabela.loc[0:4]
    cabecalho.columns = ['col1', 'col2', 'col3', 'D', 'col4', 'col5']
    del cabecalho['D']
    print(cabecalho)

    # Criar tabela de perfi estratigrafico
    perfil_estratigrafico = tabela.drop(tabela.index[0:6])
    perfil_estratigrafico.columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']

    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col2'].notna()]

    perfil_estratigrafico[['col7', 'col8']] = perfil_estratigrafico['col2'].str.rsplit(" ", 1, expand=True)
    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col8'].notna()]

    perfil_estratigrafico['col8']= pd.to_numeric(perfil_estratigrafico['col8'], errors='coerce')
    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col8'].notna()]

    print(perfil_estratigrafico['col8'])
    perfil_estratigrafico = 0
    cabecalho = 0
