
# Pipeline ETL com python:
## História da aplicação:
    Minha esposa faz rankeamento de forma manual de campanhas de vendas para empresa onde ela trabalha, observando-a percebi que poderia ajuda-la a automatizar e ganhar tempo com esse rank. Com isso e com a tarefa solicitada pela DIO sobre pipeline e ETL.
    Fiz uma aplicação onde extraiu as informações, transformo-as e por fim exporto ela para um novo arquivo , finalizando esse processo.

- ## Extract:
    Aqui extraimos as informaçoes muitas das vezes através vinda oriúndas do excel, vamos pegar esse arquivo deixar na pasta do código e iremos extrair/ler e consequentementes depois trata-lá.
    Vamos importar o pandas com o ALIAS pd e o numpy com ALIAS np. Vamos então ler o arquivo em excel utilizando o pd.read_excel.

- ## Transform:
    Vamos aqui transformar os dados lidos anteriormentes, nesse caso em especificos vamos transformar os nomes das colunas para nomes mais amigáveis e ou de acordo com a necessidade. Então faremos uma nova lista com os novos nomes das colunas que iremos utilizar.
    Vamos puxar os dados desse pdf para o pandas utilizando o "dataframe" , depois transformar esse dataframe com os novos parametros (novos nomes para as colunas), lembrando que aqui vamos ter um produto como base, onde iremos ranquear o vendedor de acordo com a venda desse produto, sendo que quando necessários poderiamos mudar os nomes dessas colunas ou nome dos produtos que seriam ranqueados.

- ## Load:
    Por fim, vamos pegar esse novo dataframe e trazer ele para um novo arquivo em excel. Trazendo então um resultado final com um ranqueamento por produto selecionado dentro daquele arquivo extraído.


## Observações:
O código vai estar comentado para melhorar o entendimento sobre essa aplicação.
    