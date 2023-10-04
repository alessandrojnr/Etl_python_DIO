import pandas as pd
import numpy as np
import PySimpleGUI as sg
## variáveis criadas para receber os parametros necessários

list_remedios = []
nome_medicamento = ""

# Layout da janela de interface

layout = [
    [sg.Text("Digite o nome do medicamento : "), sg.InputText(key="-REMEDIO-")],
    [sg.Button("Adicionar")],
    [sg.Button("Fim")]
]

# Criando a janela
window = sg.Window("ETL Rankeamento de vendedores", layout)


# Loop para capturar os eventos da janela
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Adicionar":
        nome_medicamento = values["-REMEDIO-"]
        list_remedios.append(nome_medicamento)
        [sg.popup("Valor adicionado com sucesso, caso queira adicione outro valor ou finalize o programa.")]
    elif event == "Fim":
        break
        

# Fechando a janela
window.close()

## Variavéis que iremos utilizar para transformar os dados lidos

list_remedios.append(nome_medicamento)
new_columns = ["Unidade Negocio", "Vendedor", "Remedio", "Quantidade"]
df_new = pd.DataFrame(columns=new_columns)
list_row = []

rename_columns = [f'coluna{i+1}' for i in range(22)]

## EXTRAINDO os dados , Esse arquivo esta na mesma pasta do programa, sem cabecario.
df = pd.read_excel("RELATORIO_DE_VENDA_MAIO_3.xls", header=None)

## Tratando os dados utilizando o dataframe e renomeando. Esse arquivo tem 22 colunas, poderiamos usar um len. Mas aqui fizemos o uso do valor final.
df.columns = rename_columns
df = df.dropna(axis=0, how='all')
df = df.replace(np.nan, '')
df = df.astype(str)

#renomeando as colunas  e fazendo uma iteração para verificar se o vendedor fez a venda do "REMEDIO" solicitado pelo usuário
"""
coluna1 - Un Neg
coluna2 - Remedio
coluna4 - Vendedor
coluna8 - Quantidade
"""
vl_col1, vl_col2, vl_col4, vl_col8 = None, None, None, None

for index, row in df.iterrows():
    vl_col2_tmp = row['coluna2'][row['coluna2'].find(":")+1:].strip()

    if row['coluna1'].startswith('Un'):
        vl_col1 = row['coluna1']

    if vl_col2_tmp in list_remedios:
        vl_col2 = vl_col2_tmp
    elif row['coluna2'] and row['coluna2'] not in list_remedios:
        vl_col2 = None

    if row['coluna4'] and row['coluna4'] != "Usuário Orçamento":
        vl_col4 = row['coluna4']
    else:
        vl_col4 = None

    if row['coluna8']:
        vl_col8 = row['coluna8']
    else:
        vl_col8 = None

    if all([vl_col1, vl_col2, vl_col4, vl_col8]):
        new_data = {"Unidade Negocio": vl_col1,
                    "Vendedor": vl_col4,
                    "Remedio": vl_col2,
                    "Quantidade": int(vl_col8)}

        list_row.append(new_data)

# Após tratar esse dado, foi gerado uma lista com um dicionário dentro. Esse dicionário tem chaves iguais. Para isso iremos pivotar onde os valores da chave "quantidade" serão somados para cada chave Vendedor .

df_new = pd.concat([df_new, pd.DataFrame(list_row)], ignore_index=True)
pivot = pd.pivot_table(df_new,
                       values = "Quantidade",
                       aggfunc= sum,
                       index = "Vendedor",
                       columns= "Remedio")
#df_new.to_excel("final.xlsx", index=False)

#LOAD 
pivot.to_excel("Final.xlsx")
