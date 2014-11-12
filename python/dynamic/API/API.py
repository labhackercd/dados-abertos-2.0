#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, request
from mongo_configuration.Mongo_Utils import json_return
from mongo_configuration.Mongo_Configuration import MongoConfiguration
from API_Configuration import API_Configuration


# Criando a aplicacao do Flask
app = Flask(__name__)

# Criando as configuracoes da API
api_configuration = API_Configuration()

# Criando a conexão do mongo com contexto do banco de dados
mongo = MongoConfiguration().flask_context(app)


# Lim é o limitador de retorno e o off significa quantas proposicoes serao puladas (isso é feito para se ter consultas
# paginadas)

@app.route("{API}/proposicoes.json".format(API=api_configuration.BASE_URL), methods=['GET'])
def get_proposicoes():

  if request.method == 'GET':

    # Limitando a Consulta
    lim = int(request.args.get('limit', 2000))

    # Páginando a Consulta
    off = int(request.args.get('offset', 0))

    params = {
        'legislatura': request.args.get('legislatura'),
        'autor': request.args.get('autor'),
        'partido_politico': request.args.get('partido'),

    }

    # Verificando se o limite está entre os limites de consulta pre-determinados pelo API_Configuration
    if lim > api_configuration.LIMIT_DOWN and lim <= api_configuration.LIMIT_UPPER:

        # Verificando se a Consulta tem um offset não é a maior que a quantidade de dados
        registers = mongo.db.proposicoes.count()
        if off >= 0 <= registers:
            # Realizando a Consulta no MongoDB
            proposicoes = mongo.db.proposicoes.find().skip(off).limit(lim)

            return json_return(proposicoes, "proposicoes")

        else:

            return 'É necessário definir uma paginação maior que 0 e menor que {registers}'.format(registers=registers)

    else:
        return 'É necessário definir um limite positivo maior que {DOWN} e menor ou igual a que {UPPER}'.format(DOWN=api_configuration.LIMIT_DOWN,
                                                                                        UPPER = api_configuration.LIMIT_UPPER)

if __name__ == '__main__':
    app.run(debug=True)