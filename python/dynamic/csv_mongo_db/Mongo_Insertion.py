#!/usr/bin/env python
# -*- coding: utf-8 -*-

from multiprocessing.pool import ThreadPool
from csv_mongo_db.CSV_Resource import CSVResource
from mongo_configuration.Mongo_Configuration import MongoConfiguration

# Versão inicial da inserção, onde foi necessário juntar os dois arquivos da indexação e das proposicoes
def main():

    # Criando o Leitor de CSV
    csv_resource = CSVResource()
    csv_reader = csv_resource.read_file(csv_resource.CSV_PATH)

    # Criando a Conexao com o MongoDB
    mongo_connection = MongoConfiguration().general_context()

    # Navegando na Coleção de Proposicoes
    proposicoes = mongo_connection.proposicoes

    # Criando um iterador sobre o leitor do CSV
    element = iter(csv_reader)

    # Lendo o cabeçalho do arquivo CSV
    header = next(element)

    # Limpando o banco de dados
    proposicoes.drop()

    while True:
        try:
            # Para cada linha do arquivo CSV
            line = next(element)

            # Criando um dicionario com o cabeçalho e com conteúdo de cada linha
            global dictionary

            dictionary = dict(zip(header, line))

            # Formatando os dados para o MongoDB
            dictionary = csv_resource.format_toMongo(dictionary)


            # Criando uma pisicina de Threads
            pool = ThreadPool(processes=8)

             # Adicionando a indexação e a ementa com a piscina de Threads
            async_result = pool.apply_async(indexer)

            object = async_result.get()

            # Inserindo as Proposicoes no Mongo
            proposicoes_mongo = proposicoes.insert(object)

            print proposicoes_mongo

            pool.close()
        except StopIteration:
            break

def indexer():
    csv_resource_indexer = CSVResource()
    csv_reader_indexer = csv_resource_indexer.read_file(csv_resource_indexer.INDEX_PATH)


    # Criando um iterador sobre o arquivo CSV da indexação e ementa
    element_index = iter(csv_reader_indexer)

    # Lendo o cabeçalho o arquivo CSV da indexação e ementa
    header_index = next(element_index)


    while True:
        try:
            # Para cada linha do arquivoo arquivo CSV da indexação e ementa
            line_index = next(element_index)

            # Criando um dicionario com o cabeçalho e com conteúdo de cada linha
            dictionary_index = dict(zip(header_index, line_index))

            # Verificando o código da proposicão
            if dictionary['COD_PROPOSICAO_ORIGEM'] == dictionary_index['COD_PROPOSICAO_ORIGEM']:
                dictionary['TEX_EMENTA_PROPOSICAO'] = dictionary_index['TEX_EMENTA_PROPOSICAO']
                dictionary['TEX_INDEXACAO_PROPOSICAO'] = dictionary_index['TEX_INDEXACAO_PROPOSICAO']

        except StopIteration:
            break
    return dictionary


if __name__ == "__main__":
    main()