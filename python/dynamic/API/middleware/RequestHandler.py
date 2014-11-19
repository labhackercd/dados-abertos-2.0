# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Carbon.QuickTime import dataRefSelfReference
import datetime

__author__ = 'baufaker'

class Request_Handler:

    def __init__(self, request):
        self.request = request

    def receive_defaultParams(self):
        # Paginando a consulta
        self.page_number = int(self.request.args.get('page_number', 1))

        # Datas de Apresentação
        self.date_apresentacao_final = self.request.args.get('data_apresentacao_final')
        self.date_apresentacao_inicial =self.request.args.get('data_apresentacao_inicial')

        # # Datas de Veto
        self.date_veto_final = self.request.args.get('data_veto_final')
        self.date_veto_inicial =self.request.args.get('data_veto_inicial')

        ementa = self.request.args.get('ementa')
        indexacao = self.request.args.get('indexacao')


        # Parâmetros que serão utilizados como filtros
        self.params = {
            'NUM_LEGISLATURA_APRESEN': self.request.args.get('legislatura'),
            'NOM_PROPOSICAO': self.request.args.get('cod_proposicao'),
            'NOM_PARLAMENTAR': self.request.args.get('autor'),
            'SIG_TIPO_PROPOSICAO': self.request.args.get('tipo_proposicao'),
            'COD_SEXO': self.request.args.get('cod_genero'),
            'SIG_PARTIDO_POLITICO': self.request.args.get('partido_politico'),


        }


    def validate_params(self, params):
        # Se a paginação for negativa
        if self.page_number <= 0:
            raise AttributeError

        # Nesta validação foram utilizadas uma porta lógica XOR  de forma que se uma data inicial for
        # inserida é necessária que outra também esteja e vice e versa

        bool_veto = (bool(self.date_veto_inicial) != bool(self.date_veto_final))
        bool_apresentacao = (bool(self.date_apresentacao_inicial) != bool(self.date_apresentacao_final))

        # Validando a XOR de cada uma datas com uma OR
        if bool_veto or bool_apresentacao:
            raise LookupError

        if (self.date_veto_final and self.date_veto_inicial  != None):

                # Convertendo as Datas de Veto e incluindo nos parâmetros

                self.date_veto_final = datetime.datetime.strptime(self.date_veto_final, "%d/%m/%Y")
                self.date_veto_inicial = datetime.datetime.strptime(self.date_veto_inicial, "%d/%m/%Y")
                self.params.update({'DAT_VETO_TOTAL': {"$gte": self.date_veto_inicial, "$lte": self.date_veto_final }})

                if (self.date_apresentacao_inicial and self.date_apresentacao_final != None):

                    # Convertendo as datas de apresentação

                    self.date_apresentacao_inicial = datetime.datetime.strptime(self.date_apresentacao_inicial, "%d/%m/%Y")
                    self.date_apresentacao_final = datetime.datetime.strptime(self.date_apresentacao_final, "%d/%m/%Y")
                    self.params.update({'DATAPRESENTACAOPROPOSICAO': {"$gte": self.date_apresentacao_inicial, "$lte": self.date_apresentacao_final }})




        # Filtrando o dicionário, para retirar campos que não foram utilizados na consulta
        self.filter_dictparams(params, None)
        self.filter_dictparams(params, {"$regex": None })
        self.filter_dictparams(params, {"$gte": None, "$lte": None})



    def filter_dictparams(self, params, pattern):
        # Retirando os campos do dicionário de acordo com o padrão solicitado
        self.params = dict(filter(lambda x: x[1] != pattern, self.params.iteritems()))