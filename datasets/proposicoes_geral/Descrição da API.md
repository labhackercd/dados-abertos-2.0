# API Piloto dos Dados Abertos 2.0

## Descrição da API

A API 2.0 dos Dados abertos de proposições foi desenvolvida utilizando a linguagem de programação Python, 
o framework Flask e o banco de dados: MongoDB.

## Forma de Consulta e Versionamento da API


## Retorno da API

A primeira versão do API implementa o retorno dos dados em formato [JSON](http://pt.wikipedia.org/wiki/JSON). 

No qual o retorno inclui os dados em si, e um vetor JSON (json_array) com alguns metadados:

'Limite de Exibição por Página'
'Página Atual' 
'Total de Páginas'
'Total de Resultados'
'Erro'

Por padrão a consulta da API está paginada a quantidade de resultados informados no 'Limite de Exibição por página', logo para se consultar os próximos registros é necessário utilizar o parâmetro page_number de forma a avançar na pesquisa até o número 'Total de Páginas'.

Em um exemplo teórico:

URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?legislatura=54&page_number=2


O Campo page_number, caso não seja informado, assume o valor 1.

## Utilização da API dos Dados Abertos 2.0

## Possíveis Filtros nos dados de Proposição

A primeira versão da API têm como possíveis filtros:

* Número da Legislatura
* Nome do Parlamentar autor da proposição
* Código da Proposição
* Tipos de Proposição
* Gênero do Parlamentar
* Partido Político

* Data de Veto
* Data de Apresentação


* Palavras constantes na Ementa do Projeto
* Palavras constantes na Indexação do Projeto

## Parâmetros para cada filtro

Exemplo - Filtro: Campo a ser utilizado

Número da Legislatura: legislatura
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?legislatura=54

Atualmente os valores possíveis para legislatura são:

* 51 (período que engloba 01/01/1998 a 31/12/2001) 
* 52 (período que engloba 01/01/2002 a 31/12/2005)
* 53 (período que engloba 01/01/2006 a 31/12/2010)
* 54 (período que engloba 01/01/2011 a 31/12/2014)

Código da Proposição: cod_proposicao
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?cod_proposicao=PEC 300/2002

Nome do Parlamentar Autor da proposição: autor
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?autor=Nome do Parlamentar

Tipo Propositivos: tipo_proposicao
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?tipo_proposicao='PEC'

Os valores possíveis para tipo_proposicao são:

* PEC - Projeto de Emenda a Constituição
* PLP - Projeto de Lei Complementar
* PL - Projeto de Lei Ordinária
* PRC - Projetos de Resoluções
* PDC - Projeto de Decreto Legislativo
* MPV - Medida Provisória

Gênero do Parlamentar Autor da Proposição: cod_genero
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?cod_sexo='F'

os valores possíveis de utilização para cod_genero são: 

* F - Feminino
* M - Masculino

Partido Político do Autor da Proposição: partido_politico
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?partido_politico=SIG

onde SIG representa a Sigla do Partido


Data de Apresentação da Proposição:
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?data_apresentacao_inicial=14/01/2013&data_apresentacao_final=14/01/2014

onde o campo data_apresentacao_inicial representa o início do intervalo desejado e o campo 
data_apresentacao_final representa o final do intervalo desejado.

Data de Veto Total da Proposição:
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?=data_veto_inicial=14/01/2013&=data_veto_final=14/01/2014

onde o campo data_veto_inicial representa o início do intervalo desejado e o campo 
data_veto_final representa o final do intervalo desejado.

Palavras na Ementa:
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?ementa=Violencia Doméstica

onde o campo ementa pode conter palavras constantes na ementa da proposição


Palavras na Indexação:
Exemplo de utilização: URL_DA_CAMARA/api-dinamica/v1.0/proposicoes.json?indexação=Violencia Doméstica

onde o campo indexação pode conter palavras constantes na ementa da proposição


    