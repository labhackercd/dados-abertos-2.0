#!/usr/bin/env python
# -*- coding: utf-8 -*-


from csv_mongo_db.CSV_Resource import CSVResource
from mongo_configuration.Mongo_Configuration import MongoConfiguration


def main():

    # Criando o Leitor de CSV
    csv_resource = CSVResource()
    csv_reader = csv_resource.read_file()

    # Criando a Conexao com o MongoDB
    mongo_connection = MongoConfiguration().general_context()

    # Navegando na Coleção de Proposicoes
    proposicoes = mongo_connection.proposicoes

    # Criando um iterador sobre o leitor do CSV
    element = iter(csv_reader)

    # Lendo o cabeçalho do arquivo CSV
    header = next(element)

     # Limpando o banco de dados do MongoDB
    proposicoes.drop()

    while True:
        try:
            # Para cada linha do arquivo CSV
            line = next(element)

            # Criando um dicionario com o cabeçalho e com conteúdo de cada linha
            dictionary = dict(zip(header, line))

            # Formatando os dados para o MongoDB
            dictionary = csv_resource.format_toMongo(dictionary)

            # Inserindo as proposições na Coleção do MongoDb
            proposicoes_mongo = proposicoes.insert(dictionary)

            print proposicoes_mongo
        except StopIteration:
            break

if __name__ == "__main__":
    main()