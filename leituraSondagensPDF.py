import tabula
import pandas as pd
import csv


def write_csv(myList):
    with open("Sondagens.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(myList)

lista_tabelas = tabula.read_pdf('RD_VTaruma_all.pdf', pages='all')
#print(len(lista_tabelas))

myRegistro = []
furoNo_anterior = None
folhaNo_anterior = None

for tabela in lista_tabelas:

    # cabecalho com colunas numerotadas
    cabecalho = tabela.loc[0:4]
    cabecalho.columns = [1, 2, 3, 'D', '4', '5']
    del cabecalho['D']
    
    # indicio do No do furo
    indicio_furoNo_folha = cabecalho[cabecalho[1] ==  'FURO No'].index[0]
    furoNo = cabecalho.iat[indicio_furoNo_folha,1]
    folhaNo = cabecalho.iat[indicio_furoNo_folha,4]
    # print(furoNo)
    # print(int(folhaNo))

    # Criar tabela de perfi estratigrafico
    perfil_estratigrafico = tabela.drop(tabela.index[0:6])
    perfil_estratigrafico.columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6']

    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col2'].notna()]

    perfil_estratigrafico[['col7', 'col8']] = perfil_estratigrafico['col2'].str.rsplit(" ", 1, expand=True)
    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col8'].notna()]

    perfil_estratigrafico['col8']= pd.to_numeric(perfil_estratigrafico['col8'], errors='coerce', downcast='integer')
    perfil_estratigrafico = perfil_estratigrafico[perfil_estratigrafico['col8'].notna()]
    perfil_estratigrafico['col8']= pd.to_numeric(perfil_estratigrafico['col8'], downcast='integer')
    # Remover a primeira linha selecionando as últimas n-1 linhas
    # perfil_estratigrafico = perfil_estratigrafico.tail(perfil_estratigrafico.shape[0] -1)
    # perfil_estratigrafico.rename(columns = {'col8': furoNo}, inplace = True)

    #print(perfil_estratigrafico['col8'])
    resistancia_sol = perfil_estratigrafico['col8'].tolist()

    if furoNo!=furoNo_anterior:
        resistancia_sol.insert(0, furoNo)
        myRegistro.append(resistancia_sol)
        furoNo_anterior = furoNo
        folhaNo_anterior = int(folhaNo)
        resistancia_sol_anterior = resistancia_sol
    elif int(folhaNo)<=folhaNo_anterior:
        print(f'Furo No: {furoNo} Floha No: {folhaNo} --> ERRO NA PAGÍNAÇÃO')
        break
    else:
        #resistancia_sol_anterior.append(resistancia_sol)
        print(f'O registro precedente: {myRegistro[-1]}')
        myRegistro[-1] = myRegistro[-1] + resistancia_sol
        furoNo_anterior = furoNo
        folhaNo_anterior = int(folhaNo)

    print(resistancia_sol)


write_csv(myRegistro)