#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
from flask import Flask, request
from config.APIConfiguration import API_Configuration
from middleware.MongoHandler import Mongo_Handler
from middleware.RequestHandler import Request_Handler
from mongo_configuration.Mongo_Configuration import MongoConfiguration


# Criando a aplicacao do Flask
from mongo_configuration.Mongo_Utils import json_return

app = Flask(__name__)

# Criando as configuracoes da API
api_configuration = API_Configuration()

# Criando a conexão do mongo com contexto do banco de dados
mongo = MongoConfiguration().flask_context(app)

# Limitando o retorno da Consulta (Parametro definido no arquivo de propriedades
lim = api_configuration.LIMIT_PAGE


@app.route("{API}/proposicoes.json".format(API=api_configuration.BASE_URL), methods=['GET'])

def get_proposicoes():

    # Criando um Handler de Requisições
    request_handler = Request_Handler(request)

    # Recebendo os parâmetros
    # TODO receber os parâmetros de Data
    request_handler.receive_defaultParams()

    # Validar os parâmetros da requisição
    # TODO Validar parâmetros de data
    try:
        request_handler.validate_params(request_handler.params)
    except AttributeError:
        return json_return({}, "proposicoes", {'error': 'A paginação deve ter um número inteiro positivo' })
    except ValueError:
        return json_return({}, "proposicoes", {'error': 'Data informada não é válida.' })
    except LookupError:
        return json_return({}, "proposicoes", {'error': 'O intervalo de datas não foi informado corretamente.' })
    # Criando um Handler do MongoDB
    mongo_handler = Mongo_Handler(mongo, lim)

    # Realizando a Consulta Páginada no MongoDB
    try:
        query = mongo_handler.evaluate_request("proposicoes",request_handler, lim)
        return query
    except OverflowError:
         return json_return({}, "", {'error': 'Página fora do intervalo da consulta' })



if __name__ == '__main__':
    app.run(debug=True)